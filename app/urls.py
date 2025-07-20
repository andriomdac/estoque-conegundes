from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),

    path('api/products/', include('products.urls')),
    path('api/brands/', include('brands.urls')),
    path('api/categories/', include('categories.urls')),
    path('api/stores/', include('stores.urls')),
    path('api/store_items/', include('store_items.urls')),
    path('api/prices/', include('prices.urls')),
    path('api/sales/', include('sales.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/sale_items/', include('sale_items.urls')),
    path('api/auth/', include('tokens.urls'))
]
