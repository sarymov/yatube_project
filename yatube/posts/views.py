from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    TEMPLATE = 'posts/index.html'
    TITLE = 'Это главная страница проекта Yatube'
    context = {
        'title': TITLE,
    }
    return render(request, TEMPLATE, context)


# Страница со списком мороженого
def group_posts(request, slug):
    TEMPLATE_2 = 'posts/group_list.html'
    TITLE_2 = 'Здесь будет информация о группах проекта Yatube'
    context_2 = {
        'title_2': TITLE_2
    }
    return render(request, TEMPLATE_2, context_2)

# Create your views here.
