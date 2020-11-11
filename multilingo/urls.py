from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from news import views

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.NewsListView.as_view(),name='home'),
    path('news/<slug>/', views.NewsDetail.as_view(), name='news-detail-en'),
    path('noticias/<slug>/', views.NewsDetail.as_view(), name='news-detail-es'),
    path('noticies/<slug>/', views.NewsDetail.as_view(), name='news-detail-ca'),
    path('nouvelles/<slug>/', views.NewsDetail.as_view(), name='news-detail-fr'),
)