from django.contrib import admin, messages
# Models
from apps.products.models import Category, Mark, UMedida, Product, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('description', 'active', 'slug')
    list_filter = ('active',)
    search_fields = ('description',)
    ordering = ('-active', 'description',)

    def message_user(self, *args): # overridden method
        pass

    def save_model(self, request, obj, form, change):
        if change:
            messages.add_message(request, messages.INFO, 'Categoria modificada exitosamente')
        else:
            messages.add_message(request, messages.INFO, f'Categoria agregada correctamente')
        super().save_model(request, obj, form, change)


class SubCategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('description', 'category', 'active', 'slug')
    list_filter = ('active', 'category')
    search_fields = ('description', 'category')
    ordering = ('-active', 'description',)

    def message_user(self, *args): # overridden method
        pass

    def save_model(self, request, obj, form, change):
        if change:
            messages.add_message(request, messages.INFO, 'SubCategoria modificada exitosamente')
        else:
            messages.add_message(request, messages.INFO, 'SubCategoria agregada correctamente')
        super().save_model(request, obj, form, change)


class MarkAdmin(admin.ModelAdmin):
    '''Admin View for Mark'''

    list_display = ('description', 'active', 'slug')
    list_filter = ('active',)
    search_fields = ('description',)
    ordering = ('-active', 'description',)

    def message_user(self, *args): # overridden method
        pass

    def save_model(self, request, obj, form, change):
        if change:
            messages.add_message(request, messages.INFO, 'Marca modificada exitosamente')
        else:
            messages.add_message(request, messages.INFO, 'Marca agregada correctamente')
        super().save_model(request, obj, form, change)


class UMedidaAdmin(admin.ModelAdmin):
    '''Admin View for Mark'''

    list_display = ('description', 'active', 'slug')
    list_filter = ('active',)
    search_fields = ('description',)
    ordering = ('-active', 'description',)

    def message_user(self, *args): # overridden method
        pass

    def save_model(self, request, obj, form, change):
        if change:
            messages.add_message(request, messages.INFO, 'Unidad de Medida modificada exitosamente')
        else:
            messages.add_message(request, messages.INFO, 'Unidad de Medida agregada correctamente')
        super().save_model(request, obj, form, change)


class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''

    list_display = ('description', 'mark', 'get_subcategory', 'active', 'price', 'reduction')
    list_filter = ('active', 'mark', 'subcategory')
    search_fields = ('description', 'mark__description', 'subcategory__description')
    ordering = ('-active', 'description')

    # Personalizar FK 
    def get_subcategory(self, obj):
        return obj.subcategory.description.title()
    get_subcategory.short_description = 'SubCategoria'
    get_subcategory.admin_order_field = 'subcategory__description'

    # Cambiar el inicio de los QuerySet
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'mark':
            kwargs['queryset'] = Mark.other_objects.show_actives()
        if db_field.name == 'subcategory':
            kwargs['queryset'] = SubCategory.other_objects.show_actives()
        if db_field.name == 'umedida':
            kwargs['queryset'] = UMedida.other_objects.show_actives()
        return super(ProductAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Mark, MarkAdmin)
admin.site.register(UMedida, UMedidaAdmin)
admin.site.register(Product, ProductAdmin)
