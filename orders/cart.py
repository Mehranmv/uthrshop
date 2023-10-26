from products.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get(CART_SESSION_ID)
        if not self.cart:
            self.cart = {}
            self.session[CART_SESSION_ID] = self.cart

    def add(self, product, quantity=1, price=None, color=None, size=None):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'photo': product.photo.url,
                'price': str(product.price),
                'color_sizes': {}
            }
        if color and size:
            sub_total = float(price) * int(quantity)
            color_size_id = f'{color}_{size}'
            if color_size_id not in self.cart[product_id]['color_sizes']:
                self.cart[product_id]['color_sizes'][color_size_id] = {
                    'color': color,
                    'size': size,
                    'quantity': int(quantity),
                    'sub_total': str(sub_total)
                }
            else:
                self.cart[product_id]['color_sizes'][color_size_id]['quantity'] += int(quantity)
                self.cart[product_id]['color_sizes'][color_size_id]['sub_total'] = str(
                    float(self.cart[product_id]['color_sizes'][color_size_id]['sub_total']) + sub_total)
        self.save()

    def remove(self, product, color=None, size=None):
        product_id = str(product.id)
        if product_id in self.cart:
            if color and size:
                color_size_id = f'{color}_{size}'
                if color_size_id in self.cart[product_id]['color_sizes']:
                    del self.cart[product_id]['color_sizes'][color_size_id]
                if not self.cart[product_id]['color_sizes']:
                    del self.cart[product_id]
            else:
                del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_dict = self.cart[str(product.id)]
            product_dict['product'] = product
            if product_dict['color_sizes']:
                color_sizes = []
                for color_size_dict in product_dict['color_sizes'].values():
                    color_sizes.append(color_size_dict)
                product_dict['color_sizes'] = color_sizes
            yield product_dict

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
