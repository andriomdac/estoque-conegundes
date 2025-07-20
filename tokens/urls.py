from django.urls import path
from .views import get_token_view, verify_token_view


urlpatterns = [
    path('get_token/', get_token_view, name='get_token'),
    path('verify_token/', verify_token_view, name='verify_token'),
]