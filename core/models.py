from django.db import models


class Categories(models.Model):  #pravimo unique kolonu u tabeli
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name  #omogucava prikaz teksta-naslov kategorije

# Ovde drzimo nase modele-nase tabele iz baze  tj.recimo:
#class Product =>tabela product u Db
class Product(models.Model):  #opis polja u tabeli DB
    title = models.CharField(max_length=200)  #slovni karakteri
    price = models.DecimalField(max_digits=10, decimal_places=2) #brojevi sa 2 decimale
    description = models.TextField(blank=True)  #text moze biti NULL -prazno
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
    #znaci da je polje category povazano stranim kljucem sa tabelom Categories
    #u slucaju da se obrise Categories, obrisace se i Product sa category
    #pomeramo Categories klasu iznad Product klase,kako bi ispostovali Cascade



