from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', include('products.urls')),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),

    
#   path('store_items/', include('stores.urls.store_item')),
#   path('prices/', include('stores.urls.price')),
#   path('sales/', include('sales.urls.sale')),
#   path('sale_items/', include('sales.urls.sale_item')),
#   path('payment_methods/', include('sales.urls.payment_method')),
#   path('stores/', include('stores.urls.store')),


]
