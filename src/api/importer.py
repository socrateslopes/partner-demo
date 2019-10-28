from flask import Blueprint, jsonify
from business.es_populator import import_populate_db

importer_api = Blueprint('import_api', __name__)


@importer_api.route('/import', methods=['POST'])
def populate_db():
    errors, inserted = import_populate_db()
    response = {"docs_inserted": inserted,
                "errors": errors}
    if inserted:
        return jsonify(response), 201
    else:
        return jsonify({"error": 'Import operation must be executed only once'}), 400
