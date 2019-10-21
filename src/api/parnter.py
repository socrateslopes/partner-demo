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
    lng = request.args.get('lng')
    doc = db.closer(lat, lng)
    if doc:
        return jsonify(doc), 200
    return 'No partner available for this location', 404
