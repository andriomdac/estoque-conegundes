import json
from decimal import InvalidOperation, Decimal, ROUND_HALF_UP
from app.utils.exceptions import FieldValidationError, NotFoundValidationError, ObjectValidationError
from django.core.validators import ValidationError

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


def validate_model_object_id(object_id, model_class, object_name):
    try:
        object_id = int(object_id)
        obj = model_class.objects.get(id=object_id)
    except model_class.DoesNotExist:
        raise NotFoundValidationError(f"{object_name} '{object_id}' does not exist")
    except (ValueError, TypeError):
        raise FieldValidationError(f"'{object_name}' ID must be a valid integer.")        

    return obj


def validate_model_object_unique_name(name, model_class, model_name):
    if model_class.objects.filter(name=name).exists():
        raise FieldValidationError(f"{model_name} with this name already exists.")
    return name


def validate_monetary_value_field(value_field, field_name):
    if not value_field:
        raise FieldValidationError(f"'{field_name}' cannot be blank.")
    try:
        value_field = Decimal(str(value_field)).quantize(Decimal("0.00"), rounding=ROUND_HALF_UP)
    except InvalidOperation:
        raise FieldValidationError(f"'{field_name}' must be a decimal")
    if value_field <= 0:
        raise FieldValidationError(f"'{field_name}' cannot be less or equal to 0 (zero).")
    return str(value_field)


def validate_and_save_model_object(object):
        try:
            object.full_clean()
            object.save()
            return object
        except ValidationError as e:
            raise ObjectValidationError(e.message_dict)