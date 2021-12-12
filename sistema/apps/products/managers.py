from django.db import models
# Models
# from apps.products.models import Mark, Category, UMedida, Product


class MarkManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter()

    def show_actives(self):
        return self.filter(active=True).order_by('description')
        

class CategoryManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter()

    def show_actives(self):
        return self.filter(active=True).order_by('description')


class SubCategoryManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter()

    def show_actives(self):
        return self.filter(active=True).order_by('description')


class UMedidaManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter()

    def show_actives(self):
        return self.filter(active=True).order_by('description')


class ProductManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter()

    def show_actives(self):
        return self.filter(active=True).select_related("mark","subcategory","umedida").order_by('description')