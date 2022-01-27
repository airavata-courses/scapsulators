from flask import Blueprint, current_app
from . import socketio
from .util_classes.producer import Producer
from .util_classes.consumer import Consumer
from .util_classes.weather_reporter import Weather_Reporter
from PIL import Image
import io, sys


bp = Blueprint('flask-producer-app', __name__)

@bp.route('/hello')
def landing_page():
    return 'Hello. This is my landing page.'


@socketio.on('connect', namespace='/kafka')
def test_connect():
    msg = 'Connection established for API Gateway to current application!\n\n'
    print(msg)
    return msg



@socketio.on('kafkaconsumer', namespace='/kafka')
def push_topic_to_consumer():
    request_topic = current_app.config.get("REQUEST_TOPIC")
    response_topic = current_app.config.get("RESPONSE_TOPIC")
    print(','.join([request_topic, response_topic, current_app.config.get('KAFKA_SERVER')]))
    my_consumer = Consumer(request_topic, kafka_server=current_app.config.get('KAFKA_SERVER'))
    last_offset = 100 # my_consumer.get_last_offset()
    my_producer = Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
    
    for request_message in my_consumer.consumer:
        print(type(request_message),request_message)
        print(f'Received a request-message from topic={request_topic}: {request_message.value}')
        wr = Weather_Reporter(feature_to_visualize='reflectivity', station='KVNX', year='2011', month='05', day='20', hour='10', minute='59')
        gif_abs_path = wr.generate_animation(download_data_dir=current_app.config.get('STATIC_DIR'))
        # r'C:\Users\vikra\OneDrive\Desktop\Vikrant\IUB_MS_DS_Coursework\Spring_22\CSCI-B649_Applied_Distributed_Systems\Project-1\Codebases-for-POCs\Vikrant-Python\kafka-miniprojects\Flask-producer\flask_producer_app\static\visualizations\KVNX\KVNX.gif'
        try:
            print("Converting the GIF image to bytes...")
            im = Image.open(gif_abs_path)
            im.seek(0)
            buffer = io.BytesIO()
            im.save(buffer, format='gif', save_all=True)
            gif_img_buffer = buffer.getvalue()
            print(f'Original Size of image bytestream will be {sys.getsizeof(gif_img_buffer)}')
            my_producer.publish(topic=response_topic, message=gif_img_buffer)
        except Exception as e:
            print(f'Something went wrong while reading/converting the image into bytearray...\n{e}')
            return f'Error. You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {response_topic}'
        
        if request_message.offset==last_offset:
            break
        my_consumer.close()
        
    return f'Reached end of messages for Kafka Topic = {request_message}'
