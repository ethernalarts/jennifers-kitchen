from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('', views.cart_detail, name="cart_detail"),
    path('items', views.cart_items, name="cart_items"),
    path('add/<int:product_id>/', views.cart_add, name="cart_add"),
    path('remove/<int:product_id>/', views.cart_remove, name="cart_remove"),
]
