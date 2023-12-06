from django.shortcuts import render
from django.http import HttpResponse

def sobre(request):
    return render (request, 'index.html')

def aff(request):
    return render (request, 'pagina2.html')

# Create your views here.
