from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return render(request,"anasayfaeski.html")

def anasayfa2(request):
    return render(request,"anasayfaeski2.html")

def gramaj(request):
    return render(request,"gramaj.html")

def giriş(request):
    return render(request,"login.html")

def profil(request):
    return render(request,"profil.html")

def kayıt(request):
    return render(request,"kayıt.html")

def yemekyükle(request):
    return render(request,"yemekyükle.html")