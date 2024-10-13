from django.urls import path
from.import views

urlpatterns = [
    path('login/',views.user_login,name="login"),
    path('kayıt/',views.user_kayıt,name="kayıt"),
    path('profil/',views.user_profil,name="profil"),
    path('logout/',views.user_logout,name="logout"),
]
