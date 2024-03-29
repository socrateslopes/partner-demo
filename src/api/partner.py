from flask import Blueprint, jsonify, request

from api import validate_schema
from business.es_operator import ElasticConn
from flasgger import swag_from

partner_api = Blueprint('partner_api', __name__, url_prefix='/partner')


@partner_api.route('/<int:id>')
@swag_from('../specs/partner_get.yml')
def get_partner(id):
    db = ElasticConn()
    doc = db.get(id)
    if doc:
        return jsonify(doc), 200
    return 'Not found', 404


@partner_api.route('/nearest')
@swag_from('../specs/partner_get_nearest.yml')
def find_nearest_partner():
    db = ElasticConn()
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    if not lat or not lng:
        return jsonify({'error': 'Both lat and lng are required parameters'}), 400
    doc = db.nearest_partner(lat, lng)
    if doc:
        return jsonify(doc), 200
    return 'No partner available for this location', 404


@partner_api.route('', methods=['POST'])
@validate_schema("partner")
@swag_from('../specs/partner_post.yml')
def create_partner():
    db = ElasticConn()
    req = request.json
    document = req.get('document')
    partner_exists = db.exists(document)
    if partner_exists:
        return jsonify({'error': f'Partner with document {document} already exists'}), 400
    result = db.create(req)
    return jsonify({'result': result}), 201
