from decimal import Decimal
from products.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(CART_SESSION_ID)
        if not self.cart:
            self.cart = {}
            self.session[CART_SESSION_ID] = self.cart

    def add(self, product, price, quantity=1, color=None, size=None):
        product_id = str(product.id) + '_' + str(color) + '_' + str(
            size)  # Include color and size in the product identifier
        if product_id not in self.cart:
            self.cart[product_id] = {
                'product_id': product_id,
                'name': product.name,
                'photo': product.photo.url,
                'price': str(price),
                'color': color,
                'size': size,
                'quantity': int(quantity),
                'sub_total': str(Decimal(price) * int(quantity)),
            }
        else:
            self.cart[product_id]['quantity'] += int(quantity)
            self.cart[product_id]['sub_total'] = str(
                Decimal(self.cart[product_id]['price']) * self.cart[product_id]['quantity'])
        self.save()

    def add_item_quantity(self, product_id, value):
        self.cart[product_id]['quantity'] = int(value)
        self.cart[product_id]['sub_total'] = str(
            Decimal(self.cart[product_id]['price']) * self.cart[product_id]['quantity'])
        self.save()
        return self.cart[product_id]['sub_total']

    def remove(self, product, color=None, size=None):
        product_id = str(product.id) + '_' + str(color) + '_' + str(
            size)  # Include color and size in the product identifier
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products = Product.objects.filter(id__in=[product_id.split('_')[0] for product_id in self.cart.keys()])
        for product in products:
            for product_id, product_data in self.cart.items():
                if product_id.split('_')[0] == str(product.id):
                    product_data['product'] = product
                    yield product_data

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        total_price = Decimal(0)
        for product_data in self.cart.values():
            total_price += Decimal(product_data['sub_total'])
        return total_price

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
