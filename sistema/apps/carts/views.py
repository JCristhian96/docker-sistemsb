from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib import messages
# MOdels
from apps.products.models import Product
from apps.carts.models import CartProducts
# Utils
from apps.carts.utils import get_or_create_cart


class CartAdd(View):
    def post(self, request, *args, **kwargs):
        cart = get_or_create_cart(request)
        product = Product.objects.get(pk=request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity', 1))
        cart_product = CartProducts.objects.create_or_update_quantity(
            cart=cart,
            product=product,
            quantity=quantity
        )

        if quantity != 1:
            msg = str(quantity) + " productos agregados al carrito"
        else:
            msg = str(quantity) + " producto agregado al carrito"

        messages.success(request, msg)    
        return redirect('ecommerce')
