from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from django.core.exceptions import ValidationError
from .helpers.image_compressor import ImageCompressor

class Categories(models.Model):  #pravimo unique kolonu u tabeli
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):    #objekat je tipa string
        return self.name  #omogucava prikaz teksta-naslov kategorije

# Ovde drzimo nase modele-nase tabele iz baze  tj.recimo:
#class Product =>tabela product u Db
class Product(models.Model):  #opis polja u tabeli DB
    #samo slovni karakteri, uz zahtev da proizvod ima bar 3 karaktera
    title = models.CharField(max_length=200,validators=[MinLengthValidator(3)])
    price = models.DecimalField(max_digits=10, decimal_places=2) #brojevi sa 2 decimale
    description = models.TextField(blank=True)  #text moze biti NULL -prazno
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,null=True)
    #znaci da je polje category povazano stranim kljucem sa tabelom Categories
    #u slucaju da se obrise Categories, obrisace se i Product sa category
    #pomeramo Categories klasu iznad Product klase,kako bi ispostovali Cascade

    # dodavanje putanje za sliku u bazi, skladisti sliku u products folde
    # dozvoljene ekstenzije za slike
    image = models.ImageField(upload_to="products/", null=True,
    validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg', 'png', 'webp'])])

    # dodavanje parametra za kolicinu proizvoda
    # (ne sme biti negativan broj)
    amount=models.PositiveIntegerField(default=0)

    #dodajemo funkciju za promo cenu:
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)

    def __str__(self):   #objekat je tipa string
        return self.title   #omogucava prikaz naziva proizvoda

    def clean(self):  #ako dodje do izmene cena, uradi ovu validaciju:
        if self.discounted_price and self.price:
            if self.discounted_price > self.price:
                raise ValidationError(
                    {"discounted_price": "Discounted price cannot be greater than the price"})

#kompresija slika (smanjenje Mb po slici prelaskom u .WEBP format)
    def save(self, *args, **kwargs):
        if self.image:
            compressor = ImageCompressor()
            compressed = compressor.compress(self.image)
            self.image.save(f"{self.image.name.split('.')[0]}.webp",
                            compressed, save=False)
            #uzeli smo ime slike i dodali .webp format na kraju
        super().save(*args, **kwargs)  #vrati se na snimanje fajlova
        # (bez ovog nece raditi)

class ProductImage(models.Model):   #za slike
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='images')
    #dozvoljene ekstenzije za slike:
    image = models.ImageField(
        upload_to="products/",
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg', 'png', 'webp'])])

    #kompresija slika (smanjenje Mb po slici prelaskom u .WEBP format)
    def save(self, *args, **kwargs):
        if self.image:
            compressor = ImageCompressor()  #ucitaj imagecompressor
            compressed = compressor.compress(self.image)  #pozovi compress metodu
            self.image.save(f"{self.image.name.split('.')[0]}.webp",
                            compressed, save=False)
            #uzeli smo ime slike i dodali .webp format na kraju, i sacuvali sliku
        super().save(*args, **kwargs)  #vrati se na snimanje fajlova
        #(bez ovog nece raditi)

    def __str__(self):
        return f"image for {self.product.title}"
