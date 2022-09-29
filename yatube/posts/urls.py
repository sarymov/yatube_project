# posts/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'
# Не подгружаются static файлы без это строки почему-то
urlpatterns = [
    path('', views.index, name='main_page'),
    path('group/<slug:slug>/', views.group_posts, name='group_list')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
