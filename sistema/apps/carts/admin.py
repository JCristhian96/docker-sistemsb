from django.contrib import admin
# MOdels
from apps.carts.models import Cart, CartProducts


class CartAdmin(admin.ModelAdmin):
    '''Admin View for CartProducts'''

    list_display = ('cart_id', 'createt_at')
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

admin.site.register(Cart, CartAdmin)
admin.site.register(CartProducts)