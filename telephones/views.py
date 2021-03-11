from django.shortcuts import render
from django.http import HttpResponse
from .models import Telephones
from .forms import TelephonesForm

def index(request):
    tel_data = Telephones.objects.all()
    return render(request, 'telephones/index.html', {'title':'Главная страница', 'tel_data':tel_data})

def create(request):
    initial = {'name': '-'}
    error = ''
    if request.method == 'POST':
        form = TelephonesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Ошибка"

    form = TelephonesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'telephones/create.html', data)
