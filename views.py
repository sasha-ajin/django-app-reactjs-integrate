from django.shortcuts import render
from django.http import HttpResponse


def frontend(request):
    return render(request, 'frontend.html')