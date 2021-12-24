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
    context['pages'] = [x if x.name != 'Index' else ref('First page', '/') for x in context['pages'] if x.name != 'Menu' and x.name != 'Registr']

    return context


def index(request):
    context = {}
    context['date'] = date.today().strftime("%d/%m/%Y")
    add_menu(context)

    if request.user.is_authenticated:
        context['username'] = request.user.username

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
from first.models import Expression

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

    expression = Expression(syntax=context['expression'])
    expression.save()

    return render(request, 'expression.html', context)

def history(request):
    context = {'expressions': Expression.objects.all()}
    return render(request, 'history.html', context)


from .forms import Str2WordsForm
from .models import Word
from django.contrib.auth.decorators import login_required

@login_required
def str2words(request):
    context = {}
    
    if request.method == 'POST':
        form = Str2WordsForm(request.POST)
        if form.is_valid():
            word = Word()
            s = form.cleaned_data['string']
            context['s'] = s
            s = s.split()
            
            context['words'] = [x for x in s if not x.isnumeric()]
            context['numbers'] = [x for x in s if x.isnumeric()]
            context['word_count'] = len(context['words'])
            context['number_count'] = len(context['numbers'])

            word.string = context['s']
            word.word_count = context['word_count']
            word.char_count = len(context['s'])
            if request.user.is_authenticated:
                word.user = request.user.username
            word.save()
        else:
            form = Str2WordsForm()
    else:
        form = Str2WordsForm()
    
    context['form'] = form
    add_menu(context)
    return render(request, 'str2words.html', context)

@login_required
def str_history(reqeust):
    context= {}
    context['words'] = Word.objects.filter(user=reqeust.user.username)
    add_menu(context)
    return render(reqeust, 'str_history.html', context)