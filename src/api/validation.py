schemas = {
    "partner": {
        "properties": {
            "document": {
                "type": "string",
                "pattern": "(^\d{11}$)|(^\d{14}$)"
            },
            "ownerName": {
                "type": "string"
            },
            "tradingName": {
                "type": "string"
            },
            "address": {
                "$ref": "http://geojson.org/schema/Point.json"
            },
            "coverageArea": {
                "$ref": "http://geojson.org/schema/MultiPolygon.json"
            }
        },
        "required": [
            "document",
            "ownerName",
            "tradingName",
            "address",
            "coverageArea"
        ],
        "additionalProperties": False
    }
}
