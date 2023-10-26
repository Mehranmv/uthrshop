from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product
from .forms import BuyProductForm
from django.http import JsonResponse


# Create your views here.
class ProductDetailView(View):
    form_class = BuyProductForm

    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        choices = product.choices_set.all()
        pictures = {}
        sizes2 = {}
        for images in choices:
            pictures[images.color_name] = images.pictures_set.filter(choice__color_name=images.color_name)
        for sizes in choices:
            sizes2[sizes.color_name] = sizes.size_set.filter(choice__color_name=sizes.color_name).values()
        values = []
        for keys, value in sizes2.items():
            for key in value:
                values.append(key['size'])
        values = list(set(values))

        context = {
            'product': product,
            'choices': choices,
            'pictures': pictures,
            'sizes': values,
            'form': self.form_class()
        }
        return render(request, 'pages/product-details.html', context)
