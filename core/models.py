from django.db import models

# Ovde drzimo nase modele-nase tabele iz baze  tj.recimo:
#class Product =>tabela product u Db

class Product(models.Model):  #opis polja u tabeli DB
    title = models.CharField(max_length=200)  #slovni karakteri
    price = models.DecimalField(max_digits=10, decimal_places=2) #brojevi sa 2 decimale
    description = models.TextField(blank=True)  #text moze biti NULL -prazno
