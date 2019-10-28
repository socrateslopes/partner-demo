from werkzeug.exceptions import HTTPException, default_exceptions
from flask import jsonify
from src import create_app
from utils.flask_logger import FlaskLogger

app = create_app()
FlaskLogger(app)

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
