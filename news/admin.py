from django.contrib import admin
from news.models import News
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin

class NewsAdmin(TabbedTranslationAdmin):
    pass

admin.site.register(News, NewsAdmin)