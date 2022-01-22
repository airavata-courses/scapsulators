from flask import Flask, current_app, redirect, render_template, Blueprint, request
from . import producer



bp = Blueprint('flask-producer-blueprint', __name__)

@bp.route('/')
def index():
    return f'You are on the index page. Kafka server is: {current_app.config.get("KAFKA_SERVER")}'

@bp.route('/pushTopicToConsumer', methods=['GET', 'POST'])
def push_topic_to_consumer():
    request_body = request.get_data()
    my_producer = producer.Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
    topic = current_app.config.get("TOPIC_NAME")
    print(request_body, type(request_body), str(request_body))
    my_producer.publish(topic, request_body)
    return f'You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {topic}'

