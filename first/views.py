from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    return render(request, 'index.html')


def objectives(request):
    return render(request, 'objectives.html')


def mission(request):
    return render(request, 'mission.html')

def vision(request):
    return render(request, 'vision.html')