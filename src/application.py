from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

from flasgger import Swagger
from src import create_app
from utils.flask_logger import FlaskLogger

app = create_app()
FlaskLogger(app)

swagger_template = {
    'swagger': '2.0',
    'info': {
        'title': 'Partners API',
        'description': 'API for handling partners information',
        'uiversion': 3
    }
}
swagger = Swagger(app, template=swagger_template)

@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

if __name__ == '__main__':
    for ex in default_exceptions:
        app.register_error_handler(ex, handle_error)
    app.run(port=app.config['URL_SERVER_PORT'], host='0.0.0.0')
