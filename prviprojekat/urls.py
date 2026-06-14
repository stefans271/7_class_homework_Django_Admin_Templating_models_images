
from django.contrib import admin
from django.urls import path
from core.views import home
from core.views import about
from core.views import product
from core.views import user
from core.views import create_product
from core.views import save_product

#127.0.0.1:8000 ==> my page
#pokretanje servera: python3 manage.py runserver

urlpatterns = [
    path('', home),  #prazna stranica
    path('about', about),                               
    path('proizvod/<str:name>', product),   #str: mora biti string
    path('korisnik/<int:num>', user),        #int: mora biti ceo broj
    #GET metoda za pristup HTML kodu (direktan prustup svima)
    path('admin/proizvod/create', create_product),  #nova adresa
    #POST metoda za cuvanje proizvoda u bazi(pristup ogranicen-bez korisnika)
    path("admin/proizvod/save", save_product)
]
