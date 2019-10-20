from flask_log_request_id import RequestIDLogFilter, RequestID
from .app_logger import AppLogger
from .log import create_logger


class FlaskLogger:

    def __init__(self, app):
        RequestID(app)
        create_logger(log=app.logger, config=app.config, handler_filter=RequestIDLogFilter())
        AppLogger(app)
