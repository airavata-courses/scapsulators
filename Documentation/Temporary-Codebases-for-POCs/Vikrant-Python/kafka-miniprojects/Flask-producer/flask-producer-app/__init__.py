from flask import Flask

# Factory method for app creation
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config:
        app.config.from_object(test_config, silent=True)
    else:
        app.config.from_object('config')

    
    @app.route('/hello')
    def landing_page():
        return 'Hello. This is my landing page.'

    from . import routes
    app.register_blueprint(routes.bp)
    return app