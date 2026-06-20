from django.http import (HttpResponse, HttpResponseNotFound,
                         HttpResponseNotAllowed)
# protokol za komunikaciju na internetu

def user(request,num):
    return HttpResponse(f"This is user {num}") #resavamo br. usera promenljivom "num"