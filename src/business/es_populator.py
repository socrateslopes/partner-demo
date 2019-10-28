from static.data import pdvs
from static.es_def import mapping
from flask import current_app as app
from elasticsearch import Elasticsearch
from elasticsearch.client.indices import IndicesClient


def import_populate_db():
    es_host = app.config['ELASTICSEARCH']
    es_idx = app.config['ES_IDX']

    es = Elasticsearch(f'{es_host}:9200')
    idx = IndicesClient(es)
    if idx.exists(index=es_idx):
        existing_docs = es.count(index=es_idx).get('count')
        if existing_docs:
            return existing_docs, 0

        app.logger.info("Drop and creating index and mapping definition")
        idx.delete(es_idx)
    else:
        idx.create(index=es_idx, body=mapping)

    app.logger.info("Populating elasticsearch with documents")
    errors = []
    for pdv in pdvs:
        document_id = ''.join(filter(str.isdigit, pdv.get('document')))
        pdv['document'] = document_id
        del pdv['id']
        try:
            es.index(index=es_idx, body=pdv, id=document_id)
        except Exception as ex:
            app.logger.exception(ex)
            errors.append({'id': pdv.get('id'), 'description': ex.args})
    inserted = len(pdvs) - len(errors)
    return errors, inserted
