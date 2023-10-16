from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('shop/', views.ShopPageView.as_view(), name='shop_page')
]
