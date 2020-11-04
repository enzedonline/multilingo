from django.views.generic import ListView, DetailView
from .models import News
class NewsListView(ListView):
    model = News
    template_name = 'news/list.html'
    context_object_name = 'News_Items'
class NewsDetail(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'News_Item'