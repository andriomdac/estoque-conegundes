from django.urls import path
from .views import (
    sale_create_list_view, sale_detail_delete_view, activate_sale, sale_activate_view, sale_finalize_view
)


urlpatterns = [
    path('', sale_create_list_view, name='sale_create_list'),
    path('<int:sale_id>/', sale_detail_delete_view, name='sale_update_detail_delete'),
    path('activate/<int:sale_id>/', sale_activate_view, name='sale_activate'),
    path('finalize/<int:sale_id>/', sale_finalize_view, name='sale_finalize'),


]