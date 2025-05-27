from django.urls import path
from payments.views import (
     payment_method_value_create_list_view, payment_method_value_detail_delete_view
)


urlpatterns = [
    path('', payment_method_value_create_list_view, name='payment_method_create_list'),
    path('<int:payment_method_id>/', payment_method_value_detail_delete_view, name='payment_method_detail_delete'),

]
