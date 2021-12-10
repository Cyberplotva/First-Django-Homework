from django.shortcuts import render

# Create your views here.

from datetime import date

def index(request):
    contex = {}
    contex['date'] = date.today().strftime("%d/%m/%Y")
    return render(request, 'index.html', contex)

def riddle(request):
    return render(request, 'riddle.html')


def answer(request):
    return render(request, 'answer.html')
import os

class ref:
    def __init__ (self, name, url):
        self.name = name
        self.url = url

def menu(request):
    context = {}
    # Get pages' name from templates
    context['pages'] = [ref(x[:-5].capitalize(), '/' + x[:-5] + '/') for x in os.listdir('./first/templates')]
    # Filter pages
    context['pages'] = [x if x.name != 'Index' else ref('First page', '/') for x in context['pages'] if x.name != 'Menu']

    return render(request, 'menu.html', context)
