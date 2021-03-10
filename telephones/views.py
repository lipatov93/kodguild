from django.shortcuts import render
from django.http import HttpResponse
from .models import Telephones

def index(request):
    tel_data = Telephones.objects.all()
    return render(request, 'telephones/index.html', {'title':'Главная страница', 'tel_data':tel_data})

def create(request):
    return render(request, 'telephones/create.html')
 
