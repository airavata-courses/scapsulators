from flask import Flask
from utils.producer import Producer
from utils.weather_reporter import Weather_Reporter
from PIL import Image
from flask_kafka import FlaskKafka
import signal
from threading import Event
from dateutil import parser
import io, sys, json, time

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
    return 'WEATHER REPORTER: Brief introduction.\nThis microservice has a thread to constantly list to REQUEST-topic messages, and produce WEATHER_REPORT-topic messages.'




@bus.handle(app.config.get('REQUEST_TOPIC'))
def push_topic_to_consumer(consumed_message):
    """This is a function that runs as a separate thread and listens for any incoming messages over the specified Kafka-topic.
    It parses the request-parameters, queries the Weather_Reporter class, generates the GIF report, and publishes a byte-stream of the report back to the Kafka-topic for response.
    SAMPLE REQUEST-BODY: {"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}

    Args:
        consumed_message ([bytes]): The message received over configured Kafka Topic.

    Returns:
        [str]: [description]
    """
    print(f'Received a request-message from topic={app.config.get("REQUEST_TOPIC")}: {consumed_message.value}')
    my_producer = Producer(kafka_server=app.config.get('KAFKA_SERVER'))

    try:
        request_parameters = json.loads(consumed_message.value)
    except Exception as e:
        print(f'Something went wrong while trying to convert request-message to JSON...{e}')
        my_producer.publish(topic=app.config.get('RESPONSE_TOPIC'), message=b'{"msg":"Invalid JSON object..\nTry something like:\n{"visualize":"reflectivity", "station":"KVNX", "timestamp":"2018-12-25 09:27:53"}"}')
        return f'Reached end of messages for Kafka Topic = {consumed_message}'

    visualize = request_parameters.get('visualize')
    station = request_parameters.get('station')
    timestamp = request_parameters.get('timestamp')
    dtime_parsed = parser.parse(timestamp)

    wr = Weather_Reporter(
        feature_to_visualize=visualize, station=station, 
        year=str(dtime_parsed.year).zfill(2), month=str(dtime_parsed.month).zfill(2), 
        day=str(dtime_parsed.day).zfill(2), hour=str(dtime_parsed.hour).zfill(2), 
        minute=str(dtime_parsed.minute).zfill(2))
    gif_abs_path = wr.generate_animation(download_data_dir=app.config.get('STATIC_DIR'))
    # r'C:\Users\vikra\OneDrive\Desktop\Vikrant\IUB_MS_DS_Coursework\Spring_22\CSCI-B649_Applied_Distributed_Systems\Project-1\Codebases-for-POCs\Vikrant-Python\kafka-miniprojects\Flask-producer\flask_producer_app\static\visualizations\KVNX\KVNX.gif'
    
    
    try:
        print('Converting the GIF image to bytes...')
        im = Image.open(gif_abs_path)
        im.seek(0)
        buffer = io.BytesIO()
        im.save(buffer, format='gif', save_all=True)
        gif_img_buffer = buffer.getvalue()
        print(f'Original Size of image bytestream will be {sys.getsizeof(gif_img_buffer)}')
        my_producer.publish(topic=app.config.get('RESPONSE_TOPIC'), message=gif_img_buffer)
    except Exception as e:
        print(f'Something went wrong while reading/converting the image into bytearray...\n{e}')
        return f'Error. You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {app.config.get("RESPONSE_TOPIC")}'
    
    return f'Reached end of messages for Kafka Topic = {consumed_message}'


if __name__=='__main__':
    bus.run()
    listen_kill_server()
    app.run(host=app.config.get('FLASK_HOST'), port=app.config.get('FLASK_PORT'), use_reloader=False)