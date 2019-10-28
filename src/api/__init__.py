from functools import wraps

from flask import Response
from flask import current_app as app
from flask import jsonify, request
from jsonschema import FormatChecker, SchemaError, ValidationError, validate

from api.validation import schemas


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                validate(request.json,
                         schemas[schema_name], format_checker=FormatChecker())
            except ValidationError as e:
                app.logger.error(e.args[0])
                msg = '.'.join(map(str, e.path))
                ret = {"error": f"Invalid request: {msg} {e.args[0]}"}
                return jsonify(ret), 400
            except SchemaError as e:
                app.logger.error(e.args[0])
                ret = {"error": f"Schema error: {e.path[0]} {e.args[0]}"}
                return jsonify(ret), 500
            return f(*args, **kw)
        return wrapper
    return decorator
