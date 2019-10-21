from flask import Blueprint, jsonify, request
from src.business.es_operator import ElasticConn

partner_api = Blueprint('partner_api', __name__, url_prefix='/partner')


@partner_api.route('/<int:id>')
def get_partner(id):
    db = ElasticConn()
    doc = db.get(id)
    if doc:
        return jsonify(doc), 200
    return 'Not found', 404


@partner_api.route('/nearest')
def find_nearest_partner():
    db = ElasticConn()
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    doc = db.closer(lat, lon)
    if doc:
        return jsonify(doc), 200
    return 'No partner available for this location', 404
