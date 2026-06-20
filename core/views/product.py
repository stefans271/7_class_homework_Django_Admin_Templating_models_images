from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseNotAllowed)
# protokol za komunikaciju na internetu
from django.shortcuts import render  #prikazivanje web strane
from ..models import Product  #ucitavamo klasu Product iz fajla models(u drugom folderu)


def product(request,name):

    try:   #izvlacimo ime proizvoda iz bazne klase
        product = Product.objects.get(title=name)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found!")  # strana ne postoji
        # test kako da vratimo odgovor ukoliko predmet pretrage na nekoj stranici ne postoji

    #return HttpResponse(f"{product["description"]}") #resavamo skup producta
    # promenljivom "product"

    #ucitavamo product.html
    return render(request, "product.html", {"product_info": product})
    #pravimo context kako bismo prosledili product


def create_product(request):  #metodom ucitavamo novi product_create.html
    return render(request,"product_create.html")


def save_product(request): #metod za cuvanje proizvoda
    if request.method != "POST":
        return HttpResponseNotAllowed("Only POST method is allowed")

    #request=> iz trenutnog zahteva
    #POST=>request.post--iz trenutnog zahteva iz POST metode
    #.get =>uzmi podatak sa nazivom "title"
    title=request.POST.get("title")
    price=request.POST.get("price")
    description=request.POST.get("description")
    #provera da li su svi podaci prosledjeni-bez praznih polja:
    if not title or not price or not description:
        return HttpResponse("All fields are required",status=400)  #los zahtev

    product = Product(title=title,price=price,description=description)
    #ovde smo izjednacili title iz baze i title varijablu iz save_product...
    product.save()  #ovako snimamo podatke u bazi, bez konekcije i Query upita

    #status 201 => uspesno napravljen podatak
    return HttpResponse(f"this is a {title},{price},{description}",status=201)