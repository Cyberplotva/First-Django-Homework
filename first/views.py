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


from random import randint

def expression(request):
    context = {}

    signs = ['+', '-']
    result = randint(10, 99)
    context['expression'] = str(result)
    for _ in range(randint(1, 3)):
        new_num = randint(10, 99)
        sign_ind = randint(0, 4)
        if sign_ind == 0:
            result += new_num
            context['expression'] += ' + ' + str(new_num)
        else:
            result -= new_num
            context['expression'] += ' - ' + str(new_num)
    
    context['expression'] += ' = ' + str(result)

    return render(request, 'expression.html', context)
