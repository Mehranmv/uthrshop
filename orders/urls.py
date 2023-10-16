from django.urls import path
from . import views

app_name = 'urls'
urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart')
]
