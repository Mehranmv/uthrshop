from django.urls import path
from . import views
from . import ajax

app_name = 'orders'
urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/remove/', ajax.remove_from_cart, name="remove_from_cart"),
    path('cart/update_quantity/', ajax.update_quantity_cart, name="update_quantity_cart")
]