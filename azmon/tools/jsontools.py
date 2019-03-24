from datetime import datetime
import json


def _json_handler(o):
    if isinstance(o, datetime):
        return o.isoformat()
    return o


def dumps(value):
    return json.dumps(value, default=_json_handler, indent=2)
