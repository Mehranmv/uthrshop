from .models import Product
from orders.cart import Cart
from django.http import JsonResponse


def add_to_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)

        cart.add(
            product=product,
            quantity=request.POST.get('quantity'),
            price=request.POST.get('price'),
            color=request.POST.get('color'),
            size=request.POST.get('size'),
        )
        return JsonResponse({"success": "The Product Added To Cart Successfully!"})


def remove_from_cart(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)

        cart.remove(
            product=product,
            color=request.POST.get('color'),
            size=request.POST.get('size'),
        )
        return JsonResponse({"success": "The Product Removed From Cart Successfully!"})


def update_price(request):
    if request.method == 'POST':
        color = request.POST.get('color')
        size = request.POST.get('size')
        product = Product.objects.get(slug=request.POST.get('slug'))
        # Calculate the price based on color and size
        choice = product.choices_set.filter(color_name=color, size__size=size).first()
        if choice:
            price = choice.size_set.filter(size=size).values()
            if price[0]['price'] is None:
                return JsonResponse({'price': product.price})
            else:
                return JsonResponse({'price': price[0]['price']})
        else:
            return JsonResponse({'price': 'Out of Stuck'})
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)


def color_sizes(request):
    if request.method == "POST":
        color = request.POST.get('color')
        product = Product.objects.get(slug=request.POST.get('slug'))
        choice = product.choices_set.get(color_name=color)
        sizes = choice.size_set.all().values()
        values = []
        for item in sizes:
            values.append(item['size'])

        print(values)
        return JsonResponse({'sizes2': values})
