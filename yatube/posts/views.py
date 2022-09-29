# posts/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших  к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Главная страница'
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context)


# Страница со списком мороженого
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Записи сообщества'
    context = {
        'group': group,
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/group_list.html', context)
