from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(verbose_name=_('Title'),max_length=255)
    text = models.TextField(verbose_name=_('Details'))
    pub_date = models.DateTimeField(verbose_name=_('Publication Date'),default=timezone.now)
    def get_absolute_url(self):
       return (reverse('news-detail', args=[self.pk]))