from app.settings import API_LOCAL_HOST
import requests


def construct_auth_header_from_session(request):
    return {"Authorization": request.session.get("token")}


def get_sales_list(request) -> dict:
    response = requests.get(
        API_LOCAL_HOST+"sales/",
        headers=construct_auth_header_from_session(request)      
        )
    if response.status_code == 200:
        return response.json()


def get_store_items_list(request) -> dict:
    response = requests.get(
        API_LOCAL_HOST + "store_items/",
        headers=construct_auth_header_from_session(request)
    )
    if response.status_code == 200:
        return response.json()