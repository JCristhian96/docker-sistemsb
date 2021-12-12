# Module Signals
import os
import uuid
from django.utils.text import slugify


def set_codbarra_slug(instance, sender, *args, **kwargs):
    if not instance.cod_barra:
        instance.cod_barra = str(uuid.uuid4())
    instance.slug = slugify(f"{instance.description} {instance.mark}")
    

def set_slug(sender, instance , *args, **kwargs):
    
    model = sender.__name__
    if model == 'SubCategory':
        slug = f"{instance.description} {instance.category}"
        print(slug)
        instance.slug = slugify(slug)
        return instance
    
    if instance.description:
        instance.slug = slugify(instance.description)
        return instance


