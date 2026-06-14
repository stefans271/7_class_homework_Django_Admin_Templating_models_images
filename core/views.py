from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseNotAllowed)
# protokol za komunikaciju na internetu
from django.shortcuts import render  #prikazivanje web strane

products= {
        "Macbook Air 2025":{
            "price":2000,
            "description":"This is Macbook Air 2025"
        },
        "iPhone 17 Pro": {
            "price": 1300,
            "description": "This is iPhone 17 Pro with advanced titanium design"
        },
        "iPad Pro M5": {
            "price": 1100,
            "description": "This is iPad Pro M5 with Ultra Retina XDR display"
        },
        "Apple Watch Ultra 4": {
            "price": 900,
            "description": "This is Apple Watch Ultra 4 for extreme outdoor activities"
        },
        "AirPods Pro 3": {
            "price": 250,
            "description": "This is AirPods Pro 3 with noise cancellation"
        }
    }

#postoji funkcija home koja prikazuje neku poruku
def home(request):   #funkcija "home"
    # index.html prikazati sve proizvode -> domaci

    context = {
        "products": products
        # pravimo context kako bismo prosledili product
    }

    return render(request, 'index.html',context) #OK status stranice

def about(request):
    return HttpResponse("Server error- can't find the web page",status=500)
#namerno ispisan tekst za gresku servera

def product(request,name):

    product = products.get(name)
    if not product:
        return HttpResponseNotFound("Product not found!") #strana ne postoji
#test kako da vratimo odgovor ukoliko predmet pretrage na nekoj stranici ne postoji

    context={
            "product_info":product
        #pravimo context kako bismo prosledili product
        }

    #return HttpResponse(f"{product["description"]}") #resavamo skup producta
    # promenljivom "product"

    #ucitavamo product.html -> domaci
    return render(request, "product.html",context
                  ) #saljemo na HTML (index.html)

def user(request,num):
    return HttpResponse(f"This is user {num}") #resavamo br. usera promenljivom "num"

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
    #status 201 => uspesno napravljen podatak
    return HttpResponse(f"this is a {title},{price},{description}",status=201)