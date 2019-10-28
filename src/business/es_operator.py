from flask import current_app as app
from elasticsearch import Elasticsearch


class ElasticConn:
    def __init__(self):
        es_host = app.config['ELASTICSEARCH']
        self.es = Elasticsearch(f'{es_host}:9200')
        self.es_idx = app.config['ES_IDX']

    def get(self, document):
        app.logger.info(f"Querying document with id {document}")
        partner = self.es.get(index=self.es_idx, id=document)
        if partner:
            return partner.get('_source')
        return None

    def exists(self, document):
        app.logger.info(f"Checking if document with id {document} exists")
        return self.es.exists(index=self.es_idx,id=document)

    def create(self, partner):
        app.logger.info(f"Trying to create partner")
        return self.es.create(index=self.es_idx, body=partner, id=partner.get('document')).get('result')

    def nearest_partner(self, lat, lng):
        query = {
            "size": 1,
            "query": {
                "geo_shape": {
                    "coverageArea": {
                        "relation": "intersects",
                        "shape": {
                            "type": "point",
                            "coordinates": [
                                float(lng),
                                float(lat)
                            ]
                        }
                    }
                }
            },
            "sort": [
                {
                    "_geo_distance": {
                        "address.coordinates": [
                            float(lng),
                            float(lat)
                        ],
                        "order": "asc",
                        "unit": "km",
                        "mode": "min",
                        "distance_type": "arc",
                        "ignore_unmapped": True
                    }
                }
            ]
        }
        docs = self.es.search(self.es_idx, query).get('hits').get('hits')
        if docs:
            return docs[0].get('_source')
        return None
