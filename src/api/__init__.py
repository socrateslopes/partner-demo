from jsonschema import validate, SchemaError, ValidationError, FormatChecker
from flask import current_app as app
from flask import Response
import json
from enum import Enum

from functools import wraps
from flask import (
    current_app,
    jsonify,
    request,
)


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except Exception as e:
            ret = "{\"status\" : 400, \"status_desc\": \"Bad Request\" }"
            return Response(status=400, response=ret, content_type="application/json")
        return f(*args, **kw)

    return wrapper


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json, schemas[schema_name], format_checker=FormatChecker())
            except ValidationError as e:
                app.logger.error(e.args[0])
                ret = '{"status" : 400, "status_desc": "Bad Request: property ' + '.'.join(
                    map(str, e.path)) + ' - ' + e.args[0] + '" }'
                return Response(status=400, response=ret, content_type="application/json")
            except SchemaError as e:
                app.logger.error(e.args[0])
                ret = '{"status" : 400, "status_desc": "Bad request: property ' + e.path[0] + ' - ' + e.args[
                    0] + '" }'
                return Response(status=400, response=ret, content_type="application/json")
            return f(*args, **kw)

        return wrapper

    return decorator

class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        return json.JSONEncoder.default(self, obj)