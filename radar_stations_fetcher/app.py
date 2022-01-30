from flask import Flask
from utils.producer import Producer
from utils.radar_stations import Radar_Stations
from flask_kafka import FlaskKafka
from threading import Event
import signal
import sys, json

app = Flask(__name__)
app.config.from_pyfile('config.py')

INTERRUPT_EVENT = Event()
print(app.config.get('KAFKA_SERVER'))
bus = FlaskKafka(INTERRUPT_EVENT, bootstrap_servers=app.config.get('KAFKA_SERVER'), group_id=app.config.get('GROUP_ID'))


def listen_kill_server():
    signal.signal(signal.SIGTERM, bus.interrupted_process)
    signal.signal(signal.SIGINT, bus.interrupted_process)


@app.route('/')
def landing_page():
    return 'RADAR STATIONS RETRIEVER: Brief introduction.\nThis microservice produces a JSON-object for all radar stations monitored as part of NEXRAD, and produces RADAR_STATIONS-topic messages.'




@bus.handle(app.config.get('REQUEST_TOPIC'))
def push_topic_to_consumer(consumed_message):
    """This is a function that runs as a separate thread and listens for any incoming messages over the specified Kafka-topic.
    It parses the request-parameters, queries the Radar_Stations class, generates the radar-stations list, and publishes a byte-stream of the json back to the Kafka-topic for response.

    Args:
        consumed_message ([bytes]): The message received over configured Kafka Topic.

    Returns:
        [str]: [description]
    """
    print(type(consumed_message),consumed_message)
    print(f'Received a request-message from topic={app.config.get("REQUEST_TOPIC")}: {consumed_message.value}')

    radar_stations = Radar_Stations()
    stations_list = radar_stations.get_stations()
    
    try:
        print('Converting the dictionary to bytes...')
        stations_str = json.dumps(stations_list)
        print('Converted the dictionary to string...')
        stations_buffer = bytes(stations_str, encoding='utf-8')
        print(f'Original Size of image bytestream will be {sys.getsizeof(stations_buffer)}')
        my_producer = Producer(kafka_server=app.config.get('KAFKA_SERVER'))
        my_producer.publish(topic=app.config.get('RESPONSE_TOPIC'), message=stations_buffer)
    except Exception as e:
        print(f'Something went wrong while reading/converting the image into bytearray...\n{e}')
        return f'Error. You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {app.config.get("RESPONSE_TOPIC")}'
    
    return f'Reached end of messages for Kafka Topic = {consumed_message}'


if __name__=='__main__':
    bus.run()
    listen_kill_server()
    app.run(host=app.config.get('FLASK_HOST'), port=app.config.get('FLASK_PORT'), use_reloader=False)