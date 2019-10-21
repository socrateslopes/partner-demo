mapping = {
  "mappings": {
    "properties": {
      "address.coordinates": {
        "type": "geo_point"
      },
      "coverageArea": {
        "type": "geo_shape"
      }
    }
  }
}