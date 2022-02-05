from flask import Flask, request, make_response
from werkzeug import Response
from utils.weather_reporter import Weather_Reporter
from utils.radar_stations import Radar_Stations
from dateutil import parser
import sys, http

app = Flask(__name__)
app.config.from_pyfile('config.py')




@app.route('/', methods=['GET', 'POST'])
def landing_page():
    return 'WEATHER REPORTER: Brief introduction.\nThis microservice has a thread to constantly list to REQUEST-topic messages, and produce WEATHER_REPORT-topic messages. This microservice can also produce a JSON-object for all radar stations monitored as part of NEXRAD.'



@app.route('/getRadarStations', methods=['GET','POST'])
def get_radar_stations():
    """This is a function that runs as a separate thread and listens for any incoming messages over GET-Request.
    It parses the request-parameters, queries the Radar_Stations class, generates the radar-stations list, and publishes a byte-stream of the json back as a REST-response.
        request_body ([json]): The message received via REST-GET request.
    Returns:
        [str]: JSON-object for mapping geographic-regions to specific radar-station code.
    """
    if request.method=='GET':
        print(f'Received a request-message: {request}')
        response = make_response()
        
        try:
            radar_stations = Radar_Stations()
            stations_list = radar_stations.get_stations()
            stations_buffer = radar_stations.get_stations_bytestream(stations_list)
            response.status_code = http.HTTPStatus.OK
            response.data = stations_buffer
            return response
        except Exception as e:
            print(f'Something went wrong while reading the S3 directory to identify radar-stations bytearray...\n{e}')
            response.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
            response.data = f"Error. Server couldn't generate the radar-stations json object...{e}"
            return response









@app.route('/getWeatherReport', methods=['GET','POST'])
def get_weather_report():
    """This is a function that runs as a separate thread and listens for any incoming messages over REST.
    It parses the request-parameters, queries the Weather_Reporter class, generates the GIF report, and publishes a byte-stream of the report back via REST.
    SAMPLE REQUEST-BODY: {"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}

    Args:
        request_body ([json]): The message received via REST-POST request.

    Returns:
        [str]: Bytestream of the requested weather-report.
    """
    if request.method=='GET':
        print(f'Received a request-message: {request}')
        response = make_response()
        try:
            request_parameters = request.get_json()
            visualize = request_parameters.get('visualize', None)
            station = request_parameters.get('station', None)
            timestamp = request_parameters.get('timestamp', None)
            dtime_parsed = parser.parse(timestamp)

            wr = Weather_Reporter(
            feature_to_visualize=visualize, station=station, 
            year=str(dtime_parsed.year).zfill(2), month=str(dtime_parsed.month).zfill(2), 
            day=str(dtime_parsed.day).zfill(2), hour=str(dtime_parsed.hour).zfill(2), 
            minute=str(dtime_parsed.minute).zfill(2))
            assert wr.check_params_valid()==1


        except Exception as e:
            response.status_code = http.HTTPStatus.BAD_REQUEST
            response.data = f'Request:{request.data}.\nSomething went wrong while trying to convert request-message to JSON...{e}'
            return response

        
        

        try:
            wr.generate_animation(download_data_dir=app.config.get('STATIC_DIR'))
            #gif_abs_path = r'C:\Users\vikra\OneDrive\Desktop\Vikrant\IUB_MS_DS_Coursework\Spring_22\CSCI-B649_Applied_Distributed_Systems\Project-1\Codebases-for-POCs\Vikrant-Python\kafka-miniprojects\Flask-producer\flask_producer_app\static\visualizations\KVNX\KVNX.gif'
            gif_img_buffer = wr.get_image_bytestream()
            print(f'Original Size of image bytestream will be {sys.getsizeof(gif_img_buffer)}')
            response.headers.set('Content-Type', 'image/gif')
            response.headers.set('Content-Disposition', 'attachment', filename=f'{wr.gif_abs_path}.gif')
            response.status_code = http.HTTPStatus.OK
            response.data = gif_img_buffer
            return response
        except Exception as e:
            print(f'Something went wrong while reading/converting the image into bytearray...\n{e}')
            response.status_code = http.HTTPStatus.INTERNAL_SERVER_ERROR
            response.data = f"Error. Server couldn't generate the GIF image...{e}"
            return response


if __name__=='__main__':
    app.run(
        host=app.config.get('FLASK_HOST'),
        port=app.config.get('FLASK_PORT'),
        use_reloader=app.config.get('DEBUG')
        )