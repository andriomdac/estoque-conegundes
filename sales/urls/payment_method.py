from django.urls import path
from sales.views.payment_method import (
    payment_method_create_list_view, payment_method_detail_delete_view, payment_method_choice_list_view
)


urlpatterns = [
    path('', payment_method_create_list_view, name='payment_method_create_list'),
    path('<int:payment_method_id>/', payment_method_detail_delete_view, name='payment_method_detail_delete'),
    path('choices/', payment_method_choice_list_view, name='payment_method_choice_list'),


]