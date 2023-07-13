from django.shortcuts import render

from employe.models import Employe

# Create your views here.
def home(request):
    employes = Employe.objects.all()   
    return render(request, 'index.html', {'employes': employes}) 