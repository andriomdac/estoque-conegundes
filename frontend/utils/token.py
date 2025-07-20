from app.settings import API_LOCAL_HOST
import requests
import json
from icecream import ic


def get_token(username:str, password:str) -> dict:
    response = requests.post(
        url=API_LOCAL_HOST+"auth/get_token/",
        json={"username": username, "password": password}
        ).content
    return json.loads(response)[0]


def verify_token(token:str) -> dict:
    response = requests.post(
        API_LOCAL_HOST+"auth/verify_token/",
        headers={"Authorization": token}
        )
    if response.status_code == 200:
        return True
    return False

    