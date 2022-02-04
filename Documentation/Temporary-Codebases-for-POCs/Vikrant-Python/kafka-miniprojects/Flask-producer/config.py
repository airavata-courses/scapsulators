import os
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
REQUEST_TOPIC = 'REQUEST'
RESPONSE_TOPIC = 'WEATHER_REPORT'
KAFKA_SERVER = 'localhost:9092'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'flask-producer-app', 'static')