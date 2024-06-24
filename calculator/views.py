from django.http import HttpResponse
from django.shortcuts import render, reverse
from datetime import datetime
import os


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать рецепты': reverse('index')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def index(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    template_name = 'calculator/index.html'
    tr = ''

    recipe = {

    }
    hg = request.path
    for iu in DATA[hg[1:-1]]:
        if 'servings' in request.GET:
            recipe[iu.title()] =round( DATA[hg[1:-1]].get(iu) * int(request.GET['servings']), 2)
        else:
            recipe[iu.title()] = round(DATA[hg[1:-1]].get(iu), 2)
    context = {
        'recipe': recipe
    }
    return render(request, template_name, context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
