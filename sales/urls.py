from django.urls import path
from .views import (
    sale_create_list_view, sale_detail_delete_view
)


urlpatterns = [
    path('', sale_create_list_view, name='sale_create_list'),
    path('<int:sale_id>/', sale_detail_delete_view, name='sale_update_detail_delete'),

]