from django.urls import path
from .views.home import home
from .views.auth import login_view, logout_view
from .views.sales import sales_list_view
from .views.products import store_items_list_view


urlpatterns = [
    path('', home, name='home'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),

    path('sales/', sales_list_view, name='sales_list'),
    path('store_items/', store_items_list_view, name='store_items_list')

]