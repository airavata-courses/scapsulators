import os
DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
TOPIC_NAME = 'INFERENCE'
KAFKA_SERVER = 'localhost:9092'