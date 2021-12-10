from django.shortcuts import render

# Create your views here.

from datetime import date



import os

class ref:
    def __init__ (self, name, url):
        self.name = name
        self.url = url

def add_menu(context):
    # Get pages' name from templates
    context['pages'] = [ref(x[:-5].capitalize(), '/' + x[:-5] + '/') for x in os.listdir('./first/templates')]
    # Filter pages
    context['pages'] = [x if x.name != 'Index' else ref('First page', '/') for x in context['pages'] if x.name != 'Menu']

    return context


def index(request):
    context = {}
    context['date'] = date.today().strftime("%d/%m/%Y")
    add_menu(context)
    return render(request, 'index.html', context)


def riddle(request):
    context = {}
    add_menu(context)
    return render(request, 'riddle.html', context)


def answer(request):
    context = {}
    add_menu(context)
    return render(request, 'answer.html', context)

def multiply(request):
    context = {}
    add_menu(context)
    return render(request, 'multiply.html', context)


def process(request):
    context = {}
    add_menu(context)
    if request.method == 'POST':
        context = {}
        context['number'] = request.POST.get('number_field', None)
        
        n = int(context['number'])
        l = []
        for i in range(1, 11):
            l.append(str(n) + ' * ' + str(i) + ' = ' + str(n * i))
        context['table'] = l

        add_menu(context)
        return render(request, 'multiply.html', context)