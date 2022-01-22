from django.shortcuts import render
from django.http import HttpResponse


def frontend_view(request):
    return render(request, 'frontend.html')
