from django.urls import path

from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='accounts_register'),
    path('login/', views.UserLoginView.as_view(), name='accounts_login'),
    path('logout/', views.UserLogoutView.as_view(), name='accounts_logout'),
    path('profile/', views.UserProfileView.as_view(), name='accounts_profile')
]
