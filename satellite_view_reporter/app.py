#from flask import Flask, request, make_response
#from asyncio import constants
from math import prod
from utils.consumer import Consumer
from utils.producer import Producer
from utils.satellite_view_reporter import Satellite_View_Reporter
from config import *
from dateutil import parser
import http, json, os



'''
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
            target_filename = svr.download_merra_subset(download_data_dir=app.config.get('STATIC_DIR'))
            parsed_json = svr.convert_response_to_json(filename=target_filename)
            json_res = svr.parse_json_dataset(parsed_json)
            json_res = json.dumps(json_res).encode('utf-8')
            print(f'Created your dataset...{type(json_res)}\n{json_res}\n')
            print(f'KAFKA_SERVER={app.config.get("KAFKA_SERVER")} , RESPONSE_TOPIC={app.config.get("RESPONSE_TOPIC")}')
            my_producer = Producer(kafka_server=app.config.get('KAFKA_SERVER'))
            my_producer.publish(topic=app.config.get('RESPONSE_TOPIC'), message=json_res)
            response.status_code = http.HTTPStatus.OK
            response.data = f'Created your dataset...\n{json_res}'
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
'''

def get_satellite_view_data(message):
    """It parses the request-parameters, queries the Satellite_View_Reporter class, generates the parsed clean-dataset, and publishes a byte-stream of the report back via Kafka.
    Kafka-topic used for reading requests of dataset: REQUEST_REPORT
    Kafka-topic used for responding with parsed dataset: WEATHER_REPORT
    Sample REQUEST_REPORT body: {"visualize":"LWGNTICE", "timestamp":"2018-09-01 09:27:53"}

    Args:
        message ([json]): Kafka-message received over REQUEST_REPORT.

    Returns:
        [str]: Bytestream of the requested satellite-view-report.
    """
    try:
        request_parameters = message.value
        request_parameters = json.loads(request_parameters)
        visualize = request_parameters.get('visualize', None)
        timestamp = request_parameters.get('timestamp', None)
        dtime_parsed = parser.parse(timestamp)
        
        svr = Satellite_View_Reporter(
            feature_to_visualize=visualize,
            year=str(dtime_parsed.year).zfill(2),
            month=str(dtime_parsed.month).zfill(2), 
            day=str(dtime_parsed.day).zfill(2))
        assert svr.check_params_valid()==1
    
        target_filename = svr.download_merra_subset(download_data_dir=STATIC_DIR)
        parsed_json = svr.convert_response_to_json(filename=target_filename)
        json_res = svr.parse_json_dataset(parsed_json)
        json_res = json.dumps(json_res).encode('utf-8')
        print(f'Created your dataset...{type(json_res)}\n')
    except AssertionError as e:
        json_res = json.dumps(f'ERROR: Something went wrong for Request:{request_parameters}.\nPlease try again with proper parameters...{e}').encode('utf-8')
    except Exception as e:
        json_res = json.dumps(f'ERROR: Something went wrong while reading the MERRA subset of data...\n{e}').encode('utf-8')
    finally:
        print(json_res)
        return json_res



if __name__=='__main__':
    print(KAFKA_SERVER, REQUEST_TOPIC, RESPONSE_TOPIC)
    producer = Producer(kafka_server=KAFKA_SERVER)
    consumer = Consumer(topic_to_consume=REQUEST_TOPIC, kafka_server=KAFKA_SERVER)
    for message in consumer.consume():
        print(message.value)
        json_res = get_satellite_view_data(message)
        producer.publish(topic=RESPONSE_TOPIC, message=json_res)