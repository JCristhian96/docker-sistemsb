from django.db import models


class BaseStore(models.Model):
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False, blank=False, null=False)

    class Meta:
        abstract = True
