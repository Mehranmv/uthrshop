from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product


# Create your views here.
class ProductDetailView(View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        context = {
            'product': product
        }
        return render(request, 'pages/product-details.html', context)
