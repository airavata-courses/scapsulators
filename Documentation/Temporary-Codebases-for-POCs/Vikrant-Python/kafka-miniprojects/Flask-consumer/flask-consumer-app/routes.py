from flask import redirect, Blueprint, current_app
from . import consumer, producer
import PIL.Image as Image, io, os, shutil

bp = Blueprint('flask-consumer-blueprint', __name__)

@app.route('/')
@cross_origin()
def home():
    return send_from_directory('/app', "index.html")


@bp.route('/consumeTopicFromProducer', methods=['GET', 'POST'])
def consume_topic_from_producer():

    my_producer = producer.Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
    my_producer.publish(current_app.config.get("REQUEST_TOPIC"), b"Send weather report")

    my_consumer = consumer.Consumer(
        topic_to_consume=current_app.config.get("RECEIVE_TOPIC"),
        kafka_server=current_app.config.get("KAFKA_SERVER")
    )
    consumed_data = my_consumer.consume()
    print(type(consumed_data.value))
    received_data = io.BytesIO(consumed_data.value)
    with open("temp2.gif", "wb") as f:
        shutil.copyfileobj(received_data, f)
    return f'Probably generated a local GIF image. :) Please check.'