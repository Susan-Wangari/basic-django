from django.shortcuts import render
from django.http import HttpResponse
from .models import Counties
# Create your views here.
def index(request):
    county = Counties.objects.all()
    return render(request, 'index.html', {'counties': county})

def name(request):
    # saves the name value provided in the form
    name = request.POST['name']
    return render(request, 'name.html', {'name':name})
