from src.api.health import health_api
from src.api.importer import importer_api
from src.utils.flask_logger import FlaskLogger
from src import create_app

app = create_app()
FlaskLogger(app)

app.register_blueprint(health_api)
app.register_blueprint(importer_api)

if __name__ == '__main__':
    app.run(port=app.config['URL_SERVER_PORT'], host='0.0.0.0')
