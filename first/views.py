from django.shortcuts import render

# Create your views here.

from datetime import date

def index(request):
    contex = {}
    contex['date'] = date.today().strftime("%d/%m/%Y")
    return render(request, 'index.html', contex)