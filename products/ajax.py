from django.shortcuts import render

from .models import Product
from orders.cart import Cart
from django.http import JsonResponse


def add_to_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        choices = product.choices_set.filter(
            color_name=request.POST.get('color'),
            size__size=request.POST.get('size'),
        ).first()
        if choices:
            size = choices.size_set.filter(size=request.POST.get('size')).first()
            if size.inventory != 0:
                cart.add(
                    product=product,
                    quantity=request.POST.get('quantity'),
                    price=request.POST.get('price'),
                    color=request.POST.get('color'),
                    size=request.POST.get('size'),
                )
                size.inventory -= 1
                return JsonResponse({"success": " Added To Cart Successfully!", "cart_count": cart.get_cart_counter()})
            else:
                return JsonResponse({"error": "The inventory is 0 !"})



def update_price(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        product = Product.objects.get(slug=request.POST.get('slug'))
        choice = product.choices_set.filter(color_name=color, size__size=size).first()
        if choice:
            price = choice.size_set.filter(size=size).values()
            if price[0]['inventory'] != 0:
                if price[0]['price'] is None:
                    return JsonResponse(
                        {'price': product.price, 'off_price': False, 'inventory': price[0]['inventory']})
                else:
                    if price[0]['price'] > product.price:
                        return JsonResponse(
                            {'price': price[0]['price'], 'off_price': False, 'inventory': price[0]['inventory']})
                    else:
                        return JsonResponse(
                            {'price': price[0]['price'], 'off_price': True, 'product_price': product.price,
                             'inventory': price[0]['inventory']})
            else:
                return JsonResponse({'price': 'Out of Stuck'})
        else:
            return JsonResponse({'price': 'Out of Stuck'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def color_sizes(request):
    if request.method == "POST":
        cart = Cart(request)
        color = request.POST.get('color')
        product = Product.objects.get(slug=request.POST.get('slug'))
        choice = product.choices_set.get(color_name=color)
        sizes = choice.size_set.all().values()
        picture = choice.pictures_set.first()
        values = []
        for item in sizes:
            values.append(item['size'])

        print(values)
        return JsonResponse({'sizes2': values, 'picture': picture.picture.url, "cart_count": cart.get_cart_counter()})
