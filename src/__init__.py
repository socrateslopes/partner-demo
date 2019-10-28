from src.api.health import health_api
from src.api.importer import importer_api
from src.api.partner import partner_api
import os

from flask import Flask
from .config import app_config


def create_app():
    app = Flask(__name__)
    app.config.from_object(app_config[os.getenv('FLASK_CONFIG', default='development')])

    app.config['LOGSTASH'] = os.getenv('LOGSTASH')
    app.config['ELASTICSEARCH'] = os.getenv('ELASTICSEARCH', 'elasticsearch:9200')
    app.config['ES_IDX'] = os.getenv('ES_IDX', 'pdvs')

    app.register_blueprint(health_api)
    app.register_blueprint(importer_api)
    app.register_blueprint(partner_api)
    app.config['APP_NAME'] = os.getenv('APP_NAME')
    app.config['URL_SERVER_PORT'] = int(os.getenv('URL_SERVER_PORT', 5000))

    return app
