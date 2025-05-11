from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include('products.urls.product')),
    path('brands/', include('products.urls.brand')),
    path('stores/', include('stores.urls.store')),
    path('store_items/', include('stores.urls.store_item')),
    path('prices/', include('stores.urls.price')),


]
