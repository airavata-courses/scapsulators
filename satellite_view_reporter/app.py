from math import prod
from utils.consumer import Consumer
from utils.producer import Producer
from utils.satellite_view_reporter import Satellite_View_Reporter
from config import *
from dateutil import parser
import http, json, os


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