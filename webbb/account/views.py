from django.shortcuts import render,redirect
from . forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def user_login(request):
   
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('anasayfa2')#buradaki index i anasayfa 2 ile değiştirebilirsin
                
                else:
                    messages.info(request,'Disabled account')
            
            else:
                messages.info(request,'Check Your Username and Password')
    
    else:
        form=LoginForm()

    return render(request,'login.html',{'form':form})

                

def user_kayıt(request):
    if request.method=='POST':
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            if User.objects.filter(username=username).exists():
                return render(request,'kayıt.html',{"error":"Bu username kullanılıyor."})
            
            else:
               if User.objects.filter(email=email).exists():
                return render(request,'kayıt.html',{"error":"email kullanılıyor."})
                
               else:
                   user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name, last_name=last_name)
                   user.save()
                   return redirect("login")

        else:
           return render(request,'kayıt.html',{"error":"paralo eşleşmedi"})
        
        

    else:
        return render(request,"kayıt.html")

        

def user_profil(request):
    pass

def user_logout(request):
    logout(request)
    return redirect('index')