import os

# Flask Parameters
DEBUG = os.environ.get('DEBUG', False)
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'static')
FLASK_HOST = os.environ.get('FLASK_HOST').replace('\'','')
FLASK_PORT = os.environ.get('FLASK_PORT').replace('\'','')
TARGET_LOCATION = os.environ.get('TARGET_LOCATION').replace('\'','')