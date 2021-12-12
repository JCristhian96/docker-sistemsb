import decimal
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed, post_delete
# Models
from apps.products.models import Product
# Managers
from apps.carts.managers import CartProductsManager
# Signals
from apps.carts.signals import set_cart_id, update_totals, post_save_update_totals


class Cart(models.Model):
    cart_id = models.CharField(
        unique=True,
        max_length=100,
        null=False,
        blank=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    products = models.ManyToManyField(
        Product,
        through="CartProducts"
    )    
    subtotal = models.DecimalField(
        default=0.0,
        max_digits=11, 
        decimal_places=2
    )
    total = models.DecimalField(
        default=0.0,
        max_digits=11, 
        decimal_places=2
    )
    createt_at = models.DateTimeField(
        auto_now_add=True
    )

    FEE = 0.05

    def __str__(self):
        return self.cart_id

    # Metodos
    def update_totals(self):
        self.update_subtotal()
        self.update_total()

        # if self.order:
        #     self.order.update_totals()

    def update_subtotal(self):
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
        ])
        self.save()

    def update_total(self):
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()

    def products_related(self):
        return self.cartproducts_set.select_related('product')

    # @property
    # def order(self):
    #     self.order_set.first()


class CartProducts(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        default=1
    )
    createt_at = models.DateTimeField(
        auto_now_add=True
    )

    def update_quantity(self, quantity=1):
        self.quantity = quantity
        self.save()

    objects = CartProductsManager()

    def __str__(self):
        return f"{self.product} -- {self.cart}"

# Signals
pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartProducts)
post_delete.connect(post_save_update_totals, sender=CartProducts)
m2m_changed.connect(update_totals, sender=Cart.products.through)
