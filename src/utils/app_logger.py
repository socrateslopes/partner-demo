import traceback
import uuid
from flask import request
from flask_log_request_id import current_request_id


class AppLogger:

    def __init__(self, app):
        self.app = app
        app.before_request(self.before_request)
        app.after_request(self.after_request)
        app.teardown_request(self.teardown_request)

    def before_request(self):
        if current_request_id():
            request.request_id = current_request_id()
        elif "X-Request-Id" in request.headers:
            request.request_id = f'{request.headers["X-Request-Id"]},{str(uuid.uuid4())}'
        else:
            request.request_id = str(uuid.uuid4())

        data = ""
        try:
            data = request.get_data().decode("utf-8")
        except:
            pass

        self.app.logger.info(f'REQUEST: {request.method} {request.url}')
        self.app.logger.info(f'REQUEST HEADERS: {request.method} {request.url}\n{request.headers}')
        self.app.logger.info(f'REQUEST BODY: {request.method} {request.url}\n{data}')

    def after_request(self, response):
        data = ""
        try:
            data = response.get_data().decode("utf-8")
        except Exception as e:
            pass

        self.app.logger.info(f'RESPONSE: {request.method} {request.url} {response.status}')
        self.app.logger.info(f'RESPONSE BODY: {request.method} {request.url}\n{data}')

        return response

    def error_handler(self, e):
        tb = traceback.format_exc()
        self.app.logger.error(f'ERROR: {request.method} {request.url} 5xx INTERNAL SERVER ERROR\n{tb}')
        return e.status_code if hasattr(e, 'status_code') else 500

    def teardown_request(self, e=None):
        self.app.logger.info(f'TEARDOWN: {request.method} {request.url}')
        if e:
            self.error_handler(e)
