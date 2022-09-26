# posts/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('group/<slug:slug>', views.group_posts, name='group_posts')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
