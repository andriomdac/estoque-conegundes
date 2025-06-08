from django.urls import path
from .views.home import home
from .views.auth import login_view, logout_view

urlpatterns = [
    path('', home, name='home'),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),

]