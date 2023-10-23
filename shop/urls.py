from django.urls import path
from . import views
from shop.api.urls import urlpatterns as api_urls

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<slug:category_slug>/", views.product_list, name="product_list_by_category"),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
]

urlpatterns += api_urls
