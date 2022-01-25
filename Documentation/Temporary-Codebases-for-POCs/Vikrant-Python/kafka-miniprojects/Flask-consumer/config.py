import os
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantssecretkey'
REQUEST_TOPIC = 'INFERENCE_REQUEST'
RECEIVE_TOPIC = 'WEATHER_REPORT'
KAFKA_SERVER = 'localhost:9092'