from flask import Flask, request, make_response
from utils.satellite_view_reporter import Satellite_View_Reporter
from dateutil import parser
import http

app = Flask(__name__)
app.config.from_pyfile('config.py')




@app.route('/', methods=['GET', 'POST'])
def landing_page():
    return 'SATELLITE VIEW REPORTER: Brief introduction.\nThis microservice listens to incoming messages via REST.\nIt produces a Kafka-topic message to be consumed by JAVA-Redis-Connector service when data ingestion completes.'



@app.route('/getSatelliteViewData', methods=['GET'])
def get_satellite_view_data():
    """It parses the request-parameters, queries the Satellite_View_Reporter class, generates the GIF report, and publishes a byte-stream of the report back via REST.
    SAMPLE REQUEST-BODY: {"visualize":"LWGNTICE", "timestamp":"2018-09-01 09:27:53"}

    Args:
        request_body ([json]): The message received via REST-POST request.

    Returns:
        [str]: Bytestream of the requested satellite-view-report.
    """
    if request.method=='GET':
        print(f'Received a request-message: {request}')
        response = make_response()
        try:
            request_parameters = request.get_json()
            visualize = request_parameters.get('visualize', None)
            timestamp = request_parameters.get('timestamp', None)
            dtime_parsed = parser.parse(timestamp)
            
            svr = Satellite_View_Reporter(
                feature_to_visualize=visualize,
                year=str(dtime_parsed.year).zfill(2),
                month=str(dtime_parsed.month).zfill(2), 
                day=str(dtime_parsed.day).zfill(2))
            assert svr.check_params_valid()==1


        except Exception as e:
            response.status_code = http.HTTPStatus.BAD_REQUEST
            response.data = f'Request:{request.data}.\nRequest-message invalid. Please try again with proper parameters...{e}'
            return response

        
        try:
            svr.download_merra_subset(download_data_dir=app.config.get('STATIC_DIR'), username=app.config.get('EARTHLOGIN_USERNAME'), password=app.config.get('EARTHLOGIN_PASSWORD'))
            response.status_code = http.HTTPStatus.OK
            response.data = 'Created your dataset you piece of shit.'
            return response
        except Exception as e:
            print(f'Something went wrong while reading the MERRA subset of data...\n{e}')
            response.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
            response.data = f"Error. Server couldn't ingest the MERRA dataset requested...{e}"
            return response


if __name__=='__main__':
    app.run(
        host=app.config.get('FLASK_HOST'),
        port=app.config.get('FLASK_PORT'),
        use_reloader=app.config.get('DEBUG')
        )