from django.urls import path
from .views import store_create_list_view, store_update_detail_delete_view


urlpatterns = [
    path('', store_create_list_view, name='store_create_list'),
    path('<int:store_id>/', store_update_detail_delete_view, name='store_update_detail_delete'),


]