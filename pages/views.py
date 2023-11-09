from django.shortcuts import render
from django.views import View
from products.models import Product, Brand


class IndexPageView(View):
    def get(self, request):
        return render(request, 'pages/index.html')


class ShopPageView(View):
    def get(self, request):
        products = Product.objects.all()
        brands = Brand.objects.all()
        context = {
            'products': products,
            'brands': brands
        }
        return render(request, 'pages/shop.html', context)
