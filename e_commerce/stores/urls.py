from django.urls import path

from e_commerce.stores.views import category_list, product_all, product_detail

app_name = "stores"
urlpatterns = [
    path("", product_all, name="product_all"),
    path("<slug:slug>", product_detail, name="product_detail"),
    path("shop/<slug:category_slug>/", category_list, name="category_list"),
]
