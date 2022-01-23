from flask import redirect, Blueprint, current_app
from . import consumer
import PIL.Image as Image, io, os

bp = Blueprint('flask-consumer-blueprint', __name__)

@bp.route('/')
def index():
    return f'You are on the homepage for the Flask consumer application. Kafka server: {current_app.config.get("KAFKA_SERVER")}.'



@bp.route('/consumeTopicFromProducer', methods=['GET', 'POST'])
def consume_topic_from_producer():
    my_consumer = consumer.Consumer(
        topic_to_consume=current_app.config.get("TOPIC_NAME"),
        kafka_server=current_app.config.get("KAFKA_SERVER")
    )
    consumed_data = my_consumer.consume()
    print(consumed_data, type(consumed_data))
    print(consumed_data.value)
    image = Image.open(io.BytesIO(consumed_data.value.values()))
    image.save(os.path.join(os.getcwd(),'temp.gif'))
    #return list(consumed_data.value.values())[0]
    return f'Attempted to consume and save an image.'