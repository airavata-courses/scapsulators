import os
#from dotenv import load_dotenv
#ENV_VARS_PATH = os.path.join(os.path.dirname(__file__), 'config.env')
#load_dotenv(ENV_VARS_PATH)

# Flask Parameters
DEBUG = os.environ.get('DEBUG').replace('\'','')
SECRET_KEY = os.environ.get('SECRET_KEY') or 'vikrantsecretkey'
STATIC_DIR = os.environ.get('STATIC_DIR') or os.path.join(os.path.dirname(__file__), 'static')
FLASK_HOST = os.environ.get('FLASK_HOST').replace('\'','')
FLASK_PORT = os.environ.get('FLASK_PORT').replace('\'','')