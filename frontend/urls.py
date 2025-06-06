from django.urls import path
from .views.home import home, brands_list

urlpatterns = [
    path('', home, name='home'),
    path('brands/', brands_list, name='brands_list'),
]