from flask import Flask

# Factory method to create a flask application
def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object('config')
    
    from . import routes
    app.register_blueprint(routes.bp)

    return app