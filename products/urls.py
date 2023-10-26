from django.urls import path
from . import views
from . import ajax

app_name = 'products'
urlpatterns = [
    path('product/<str:product_slug>/', views.ProductDetailView.as_view(), name='products_detail'),
    path('update_price/', ajax.update_price, name='update_price'),
    path('color/sizes/', ajax.color_sizes, name='color_sizes'),
    path('cart/add/', ajax.add_to_cart, name="add_to_cart")
]
