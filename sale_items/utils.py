from app.utils.http import get_json_from_request_body, build_json_error_response, build_json_response


def create_new_sale_item(request, response):
    """
    Create (POST) new sale_item based on request body
    """
    return build_json_response(response)