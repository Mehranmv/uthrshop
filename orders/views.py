from django.shortcuts import render
from django.views import View
from .cart import Cart


# Create your views here.
class CartView(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart.cart:
            print(cart.cart)
        return render(request, 'pages/cart.html', {'cart': cart})
