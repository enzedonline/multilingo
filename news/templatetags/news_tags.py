from django import template
from django.utils import translation
from typing import Optional, Any, Dict
from django import urls
from django.conf import settings

register = template.Library()
languages = [lang[0] for lang in settings.LANGUAGES]

@register.simple_tag 
def get_verbose_name(object): 
    return object._meta.verbose_name

@register.simple_tag 
def get_language_url(news_item, language_code):
    slugfieldname = f"slug_{language_code}"
    try:
        slug = getattr(news_item, slugfieldname)
    except AttributeError as e:
        return language_code
    news_path = settings.NEWS_PATH[language_code]
    return f"{language_code}/{news_path}/{slug}"
    
@register.simple_tag
def get_base_url(request):
    return request.build_absolute_uri('/')

@register.simple_tag
def get_verbose_field_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name.title()