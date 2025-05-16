from django.urls import path
from brands.views import (
    brand_create_list_view, brand_update_detail_delete_view
)


urlpatterns = [
    path('', brand_create_list_view, name='brand_create_list'),
    path('<int:brand_id>/', brand_update_detail_delete_view, name='brand_update_detail_delete'),

]