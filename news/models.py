from django.urls import reverse
from django.utils.translation import get_language, ugettext_lazy as _
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from django.db.models import Q

import string, random

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size)) 
  
def unique_slug_generator(instance, slugfieldname, title, new_slug = None): 
    if new_slug is not None: 
        slug = new_slug 
    else: 
        slug = slugify(title) 
    Klass = instance.__class__ 
    max_length = Klass._meta.get_field(slugfieldname).max_length
    slug = slug[:max_length]
    kwargs = {slugfieldname: slug}
    qs_exists = Klass.objects.filter(**kwargs).exists() 
    if qs_exists: 
        new_slug = "{slug}-{randstr}".format( 
            slug = slug[:max_length-5], randstr = random_string_generator(size = 4)) 
        return unique_slug_generator(instance, slugfieldname, title, new_slug = new_slug) 
    return slug
    
class News(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Page URL'), max_length = 200, blank=True, allow_unicode=True, unique=True) 
    text = models.TextField(verbose_name=_('Details'))
    pub_date = models.DateTimeField(verbose_name=_('Publication Date'), default=timezone.now)
    
    def get_absolute_url(self):
       return (reverse('news-detail', args=[self.slug]))

@receiver(pre_save, sender=News)
def pre_save_receiver(sender, instance, *args, **kwargs): 
    if instance.slug in (None, ''):
        title = getattr(instance, "title")
        result = unique_slug_generator(instance, "slug", title) 
        setattr(instance, "slug", result)
    for lang in [lang[0] for lang in settings.LANGUAGES]:
        slugfieldname = f"slug_{lang}"
        slugfield = getattr(instance, slugfieldname)
        if slugfield in (None, ''): 
            title = getattr(instance, f"title_{lang}")
            result = unique_slug_generator(instance, slugfieldname, title) 
            setattr(instance, slugfieldname, result)
            
        

