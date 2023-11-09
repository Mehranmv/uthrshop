from django.http import JsonResponse
from django.shortcuts import render

from products.models import Product
from orders.cart import Cart


def remove_from_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product_id = product_id.split('_')[0]
        print(product_id)
        product = Product.objects.get(pk=product_id)

        cart.remove(
            product=product,
            color=request.POST.get('color'),
            size=request.POST.get('size'),
        )
        return JsonResponse({"success": "The Product Removed From Cart Successfully!"})


def update_quantity_cart(request):
    if request.method == "POST":
        cart = Cart(request)
        product_id = request.POST.get('p_id')
        value = request.POST.get('quantity')
        updated_product_price = cart.add_item_quantity(product_id, value)
        return JsonResponse(
            {'success': 'The quantity of product is updated', 'updatedPrice': str(updated_product_price)})


def update_cart(request):
    if request.method == "GET":
        return render(request, "../templates/inc/mini_cart.html")
    else:
        return JsonResponse({"error": "Invalid request method"})
