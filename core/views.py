from django.http import HttpResponse #protokol za komunikaciju na internetu
from django.shortcuts import render  #prikazivanje web strane

#postoji funkcija home koja prikazuje poruku "Hello world"
def home(request):   #funkcija "home"
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is my about page")