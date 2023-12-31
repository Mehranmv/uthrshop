from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('', include('products.urls', namespace='products')),
    path('', include('accounts.urls', namespace='accounts')),
    path('', include('orders.urls', namespace='orders')),
    path('verification/', include('verify_email.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
