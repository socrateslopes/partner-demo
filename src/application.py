from src.utils.flask_logger import FlaskLogger
from src import create_app

app = create_app()
FlaskLogger(app)

if __name__ == '__main__':
    app.run(port=app.config['URL_SERVER_PORT'], host='0.0.0.0')
