from django.urls import path
from .views import (
    product_create_list_view, product_update_detail_delete_view
)


urlpatterns = [
    path('', product_create_list_view, name='product_create_list'),
    path('<int:product_id>/', product_update_detail_delete_view, name='product_update_detail_delete'),

]