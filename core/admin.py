from email.mime import image
from django.contrib import admin
from .models import Product, Categories, ProductImage
from django.utils.html import format_html

#pravimo dekorator klasu za administratorski model(http://127.0.0.1:8000/admin/auth/user/)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','title','in_stock','price','image_preview']
    def image_preview(self, obj):  #polje za prikaz slike(image)
        if obj.image:  #za sliku
            return format_html('<img src="{}" width="50" />', obj.image.url)
        return "null"

    def in_stock(self,obj): #funkcija za definisanje kolicine producta(ako je >0)
        #if obj.amount>0:
            #return "Yes"
        #return "No"
        return "Yes" if obj.amount else "No"

# Register your models here.
admin.site.register(Product, ProductAdmin)  #iz ProductAdmin uzimamo podatke za prikaz
admin.site.register(Categories)
admin.site.register(ProductImage)
