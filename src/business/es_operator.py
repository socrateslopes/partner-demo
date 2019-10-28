from flask import current_app as app
from elasticsearch import Elasticsearch


class ElasticConn:
    def __init__(self):
        es_host = app.config['ELASTICSEARCH']
        self.es = Elasticsearch(f'{es_host}:9200')
        self.es_idx = app.config['ES_IDX']

    def get(self, id):
        query = {
            "size": 1,
            "query": {
                "match": {
                    "id": id
                }
            }
        }
        docs = self.es.search(self.es_idx, query).get('hits').get('hits')
        if docs:
            return docs[0].get('_source')
        return None

    def get_by_document(self, document):
        query = {
            "size": 1,
            "query": {
                "match": {
                    "document": document
                }
            }
        }
        docs = self.es.search(self.es_idx, query).get('hits').get('hits')
        if docs:
            return docs[0].get('_source')
        return None

    def create(self, partner):
        return self.es.index(index=self.es_idx, body=partner)

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
