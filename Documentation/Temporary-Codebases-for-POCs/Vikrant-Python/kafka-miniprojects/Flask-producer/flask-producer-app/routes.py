from flask import Flask, current_app, redirect, render_template, Blueprint, request
from .util_classes.producer import Producer
from .util_classes.weather_reporter import Weather_Reporter
import cv2, io


bp = Blueprint('flask-producer-blueprint', __name__)

@bp.route('/')
def index():
    return f'You are on the index page of Producer. Kafka server is: {current_app.config.get("KAFKA_SERVER")}'

@bp.route('/pushTopicToConsumerBkp', methods=['GET', 'POST'])
def push_topic_to_consumer_bkp():
    request_body = request.get_data()
    my_producer = Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
    topic = current_app.config.get("TOPIC_NAME")
    print(request_body, type(request_body), str(request_body))
    my_producer.publish(topic, request_body)
    return f'You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {topic}'



@bp.route('/pushTopicToConsumer', methods=['GET', 'POST'])
def push_topic_to_consumer():
    request_body = request.get_data()
    topic = current_app.config.get("TOPIC_NAME")
    print(request_body, type(request_body), str(request_body))
    wr = Weather_Reporter(feature_to_visualize='reflectivity', station='KVNX', year='2011', month='05', day='20', hour='10', minute='59')
    gif_abs_path = wr.generate_animation(download_data_dir=current_app.config.get('STATIC_DIR'))
    try:
        image = cv2.imread(gif_abs_path)
        ret, buffer = cv2.imencode('.gif', image)
        buff = io.BytesIO(buffer)
        my_producer = Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
        my_producer.send("INFERENCE", buff.get_value())
    except Exception as e:
        print('Something went wrong while reading/converting the image into bytearray...\n{e}')
        return f'Error. You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {topic}'
    
    

