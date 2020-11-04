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
    path('post/<int:pk>/', views.NewsDetail.as_view(), name='news-detail'),
)