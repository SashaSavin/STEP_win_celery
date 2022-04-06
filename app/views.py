from django.shortcuts import render
from .tasks import add


def index(request):
    add.delay(1, 2)
    return render(request, 'index.html')


