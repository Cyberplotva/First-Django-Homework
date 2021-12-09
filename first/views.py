from django.shortcuts import render

# Create your views here.

def riddle(request):
    return render(request, 'riddle.html')


def answer(request):
    return render(request, 'answer.html')