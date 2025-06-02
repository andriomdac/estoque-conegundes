from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('stores/', include('stores.urls')),
    path('store_items/', include('store_items.urls')),
    path('prices/', include('prices.urls')),
    path('sales/', include('sales.urls')),
    path('payments/', include('payments.urls')),
    path('sale_items/', include('sale_items.urls')),
    path('auth/', include('tokens.urls'))
]
