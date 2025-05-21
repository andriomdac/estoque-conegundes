import json
from decimal import InvalidOperation, Decimal, ROUND_HALF_UP


def validate_request_body(request, required_fields=None):

    try:
        data = json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        raise ValueError("Invalid request body.")

    if required_fields:
        missing_fields = []
        for field in required_fields:
            if field not in data:
                missing_fields.append(field)
        if missing_fields:
            raise ValueError(f"Missing required fields: {missing_fields}")
    return data