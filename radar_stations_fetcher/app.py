from flask import Flask, request, make_response
from utils.radar_stations import Radar_Stations
import http

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/', methods=['GET','POST'])
def landing_page():
    return 'RADAR STATIONS RETRIEVER: Brief introduction.\nThis microservice produces a JSON-object for all radar stations monitored as part of NEXRAD.'


@app.route('/getRadarStations', methods=['GET','POST'])
def push_topic_to_consumer():
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
            response.status = http.HTTPStatus.INTERNAL_SERVER_ERROR
            response.data = f"Error. Server couldn't generate the radar-stations json object...{e}"
            return response


if __name__=='__main__':
    app.run(
        host=app.config.get('FLASK_HOST'),
        port=app.config.get('FLASK_PORT'),
        use_reloader=app.config.get('DEBUG')
        )