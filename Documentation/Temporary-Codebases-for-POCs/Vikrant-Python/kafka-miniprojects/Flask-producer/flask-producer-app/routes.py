from flask import current_app, redirect, render_template, Blueprint, request
from .util_classes.producer import Producer
from .util_classes.weather_reporter import Weather_Reporter
from PIL import Image
import io, os, sys


bp = Blueprint('flask-producer-blueprint', __name__)

@bp.route('/')
def index():
    return f'You are on the index page of Producer. Kafka server is: {current_app.config.get("KAFKA_SERVER")}'



@bp.route('/pushTopicToConsumer', methods=['GET', 'POST'])
def push_topic_to_consumer():
    request_body = request.get_data()
    request_topic = current_app.config.get("REQUEST_TOPIC")
    response_topic = current_app.config.get("RESPONSE_TOPIC")
    print(request_body, type(request_body), str(request_body))
    wr = Weather_Reporter(feature_to_visualize='reflectivity', station='KVNX', year='2011', month='05', day='20', hour='10', minute='59')
    gif_abs_path = wr.generate_animation(download_data_dir=current_app.config.get('STATIC_DIR')) #os.path.join(current_app.config.get('STATIC_DIR'),'visualizations\KVNX\KVNX.gif')
    try:
        print("Converting the GIF image to bytes...")
        im = Image.open(gif_abs_path)
        im.seek(0)
        buffer = io.BytesIO()
        im.save(buffer, format='gif', save_all=True)
        gif_img_buffer = buffer.getvalue()
        print(f'Original Size of image bytestream will be {sys.getsizeof(gif_img_buffer)}')
        my_producer = Producer(kafka_server=current_app.config.get('KAFKA_SERVER'))
        my_producer.publish(topic=response_topic, message=gif_img_buffer)
    except Exception as e:
        print(f'Something went wrong while reading/converting the image into bytearray...\n{e}')
        return f'Error. You are inside the function for publishing a topic to a consumer using Kakfa. Kafka topic is: {response_topic}'
    finally:
        return f'Attempted to send an image using Kafka for Topic = {response_topic}'
    
    

