from django.urls import path
from categories.views import (
    category_create_list_view, category_update_detail_delete_view
)


urlpatterns = [
    path('', category_create_list_view, name='category_create_list'),
    path('<int:category_id>/', category_update_detail_delete_view, name='category_update_detail_delete'),

]