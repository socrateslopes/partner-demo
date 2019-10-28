from flask import Blueprint, jsonify
from flasgger import swag_from

health_api = Blueprint('health_api', __name__)


@health_api.route('/health')
@swag_from('../specs/health.yml')
def health():
    return jsonify({'ok': True}), 200
