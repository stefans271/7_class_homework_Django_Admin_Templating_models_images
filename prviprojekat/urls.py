from django.conf import settings
from django.urls import re_path
from django.views.static import serve
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

#general.py
from core.views.general import home
from core.views.general import about
#user.py
from core.views.user import user
#product.py
from core.views.product import product
#from core.views.product import create_product
#from core.views.product import save_product

#auth_views
from django.contrib.auth import views as auth_views


#127.0.0.1:8000 ==> my page
#pokretanje servera: python3 manage.py runserver

urlpatterns = [
    path('', home),  #prazna stranica
    path('about', about),                               
    path('proizvod/<str:name>', product, name="product_page"),
    #str: mora biti string
    path('korisnik/<int:num>', user),      #int: mora biti ceo broj
    #GET metoda za pristup HTML kodu (direktan prustup svima)
    #path('admin/proizvod/create', create_product),  #nova adresa
    #POST metoda za cuvanje proizvoda u bazi(pristup ogranicen-bez korisnika)
    #path("admin/proizvod/save", save_product),
    #login strana
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html',
                                                next_page="/"), name="login_page"),
                                                #/-->ide na glavnu stranicu
    path('logout/', auth_views.LogoutView.as_view(next_page="/"),
                                                    name="logout_action"),
                                                #sa logout-a vraca na glavnu stranicu
    path('admin/', admin.site.urls),

    # putanja: /media/products/xxx.jpg
    re_path(r"media/(?P<path>.*)$", serve, {
        "document_root": settings.MEDIA_ROOT}),
]

