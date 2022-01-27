import os
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
REQUEST_TOPIC = 'REQUEST'
RESPONSE_TOPIC = 'WEATHER_REPORT'
KAFKA_SERVER = 'localhost:9092'
CORS_HEADERS = 'Content-Type'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'flask_producer_app', 'static')