from django.urls import path

from e_commerce.stores.views import *

app_name = "stores"
urlpatterns = [
    path('', all_products, name='all_products'),
    path('item/<slug:slug>/', product_detail, name='product_detail')
]
