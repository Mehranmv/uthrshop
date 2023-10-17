from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<str:product_slug>/', views.ProductDetailView.as_view(), name='product_detail')
]
