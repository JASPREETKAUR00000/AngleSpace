from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("products/", views.products_view, name="products"),
    path("buy/<int:product_id>/", views.buy, name="buy"),
    path("orders/", views.orders, name="orders"),
]
