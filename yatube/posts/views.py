from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница YaTube')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Группы')

# Create your views here.
