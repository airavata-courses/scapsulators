import os
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
TOPIC_NAME = 'INFERENCE'
KAFKA_SERVER = 'localhost:9092'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'flask-producer-app', 'static')