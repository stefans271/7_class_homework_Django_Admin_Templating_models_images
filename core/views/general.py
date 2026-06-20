from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseNotAllowed)
# protokol za komunikaciju na internetu
from django.shortcuts import render  #prikazivanje web strane
from ..models import Product  #ucitavamo klasu Product iz fajla models za tabele

#postoji funkcija home koja prikazuje neku poruku
def home(request):   #funkcija "home"
    # index.html prikazati sve proizvode

    return render(request, 'index.html', {
        "products": Product.objects.order_by("-id")[:3]})
    # [:3]znaci da vratimo samo prva 3
    # proizvoda iz baze
    # "-id" znaci da ide od zadnjeg id ka prvom iz baze
    # pravimo context kako bismo prosledili upit ka klasi Product iz baze,
    # za sve objekte kako bismo ih selektovali

def about(request):
    return HttpResponse("Server error- can't find the web page",status=500)
#namerno ispisan tekst za gresku servera