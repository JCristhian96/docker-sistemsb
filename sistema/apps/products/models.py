import os
from django.core.exceptions import NON_FIELD_ERRORS
from django.db import models
from django.db.models.signals import pre_save 
from django.utils.deconstruct import deconstructible
# Models
from apps.core.models import BaseStore
from apps.products.managers import MarkManager, CategoryManager, UMedidaManager, ProductManager, SubCategoryManager
# Signals
from .signals import set_codbarra_slug, set_slug
# Terceros
from easy_thumbnails.fields import ThumbnailerImageField


@deconstructible
class PathRename(object):

    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = f"{instance.slug}.{ext}"
        # return the whole path to the file
        return os.path.join(self.path, filename)


class Category(BaseStore):
    description = models.CharField(
        unique=True,
        max_length=100,
        error_messages={'unique':"Categoria existente."},
        verbose_name='Descripcion'
    )
    image = ThumbnailerImageField(
        upload_to=PathRename('categorys'),
        blank=True
    )

    objects = models.Manager()
    other_objects = CategoryManager()
    
    def __str__(self):
        return self.description.title()

    def clean(self):
        self.description = self.description.upper()
        return super().clean()

    class Meta:
        ordering = ['-active', 'description']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class SubCategory(BaseStore):
    description = models.CharField(
        max_length=100,
        verbose_name='Descripcion'
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = models.Manager()
    other_objects = SubCategoryManager()

    def name(self):
        return self.description
    
    def __str__(self):
        return f"{self.description.title()} - {self.category.description.title()}"

    def clean(self):
        self.description = self.description.upper()
        return super().clean()

    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ('description', 'category'):
            return "Ya existe una SubCategoria registrada con la Categoria elegida"
        else:
            return super(SubCategory, self).unique_error_message(model_class, unique_check)

    class Meta:        
        ordering = ['-active', 'description']
        unique_together = ['description', 'category',]
        verbose_name = 'Sub Categoria'
        verbose_name_plural = 'Sub Categorias'


class Mark(BaseStore):
    description = models.CharField(
        unique=True,
        max_length=50,
        error_messages={'unique':"Marca existente."},
        verbose_name='Descripcion'
    )
    image = ThumbnailerImageField(
        upload_to=PathRename('marks'),
        blank=True
    )

    objects = models.Manager()
    other_objects = MarkManager()
    
    def __str__(self):
        return self.description.title()

    def clean(self):
        self.description = self.description.upper()
        return super().clean()

    class Meta:
        ordering = ['-active', 'description']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class UMedida(BaseStore):
    description = models.CharField(
        unique=True,
        max_length=50,
        error_messages={'unique':"Unidad de Medida existente."},
        verbose_name='Descripcion'
    )

    objects = models.Manager()
    other_objects = UMedidaManager()
    
    def __str__(self):
        return self.description.title()

    def clean(self):
        self.description = self.description.upper()
        return super().clean()

    class Meta:
        ordering = ['-active', 'description']
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'


class Product(BaseStore):
    cod_barra = models.CharField(max_length=255, unique=True, editable=False)
    description = models.CharField(
        max_length=255,
        error_messages={'unique':"Producto existente."},
        verbose_name='Descripcion'
    )
    mark = models.ForeignKey(Mark, on_delete=models.CASCADE, verbose_name='Marca', )
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name='Sub Categoria')
    umedida = models.ForeignKey(UMedida, on_delete=models.CASCADE, verbose_name='Unidad de Medida')

    detail = models.TextField(blank=True, null=True, verbose_name="Detalles")

    price = models.DecimalField(
        default=0.0,
        max_digits=11, 
        decimal_places=2
    )
    reduction = models.DecimalField(
        default=0.0,
        max_digits=11, 
        decimal_places=2
    )
    stock = models.IntegerField(
        default=0
    )

    image = ThumbnailerImageField(
        upload_to=PathRename('products'),
        blank=True
    )
    
    objects = models.Manager()
    other_objects = ProductManager()

    def __str__(self):
        return f"{self.description.title()} - {self.mark}"

    def clean(self):
        self.description = self.description.upper()
        return super().clean()

    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ('description', 'mark'):
            return "Ya existe un Producto registrado con la Marca seleccionada"
        else:
            return super(Product, self).unique_error_message(model_class, unique_check)

    class Meta:
        ordering = ['-active', 'description']
        unique_together = ['description', 'mark',]
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


# Signals
pre_save.connect(set_slug, Category)
pre_save.connect(set_slug, SubCategory)
pre_save.connect(set_slug, Mark)
pre_save.connect(set_slug, UMedida)
pre_save.connect(set_codbarra_slug, Product)
