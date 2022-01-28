import os
from dotenv import load_dotenv
ENV_VARS_PATH = os.path.join(os.path.dirname(__file__), 'config.env')
load_dotenv(ENV_VARS_PATH)

# Flask Parameters
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'static')
FLASK_HOST = os.environ.get('FLASK_HOST')
FLASK_PORT = os.environ.get('FLASK_PORT')

# Kafka Parameters
REQUEST_TOPIC = os.environ.get('REQUEST_TOPIC')
RESPONSE_TOPIC = os.environ.get('RESPONSE_TOPIC')
GROUP_ID = os.environ.get('GROUP_ID')
KAFKA_SERVER = os.environ.get('KAFKA_SERVER')