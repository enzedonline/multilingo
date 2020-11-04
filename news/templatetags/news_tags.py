from django import template
from django.utils import translation
from typing import Optional, Any, Dict
from django import urls
from django.conf import settings

register = template.Library()
languages = ['es', 'ca', 'en', 'fr']
print(settings.LANGUAGES)
@register.simple_tag 
def get_base_url(url):
    base = url.split("/")
    base.pop(0)
    if base[0] in languages:
        base.pop(0)
        return("/" + "/".join(base))
    else:
        return(url) 

@register.simple_tag 
def get_verbose_name(object): 
    return object._meta.verbose_name

@register.simple_tag
def set_international_english():
    translation.activate('en-GB')
    return('')

@register.simple_tag(takes_context=True)
def translate_url(context: Dict[str, Any], language: Optional[str]) -> str:
    # url = context['request'].build_absolute_uri('/') + \
    #       language + \
    #       get_base_url(context['request'].get_full_path())
    return '' #url