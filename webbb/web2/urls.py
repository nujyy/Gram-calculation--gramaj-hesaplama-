from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    
    path("anasayfa2/",views.anasayfa2,name="anasayfa2"),
    path("gramaj/",views.gramaj,name="gramaj"),
    path("giriş/",views.giriş,name="giriş"),
    path("profil/",views.profil,name="profil"),
    path("kayıt/",views.kayıt,name="kayıt"),
    path("yemekyükle",views.yemekyükle,name="yemekyükle"),
   
]

