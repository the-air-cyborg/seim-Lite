from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'seimLiteApp/login.html',{'error':'Invalid username or password'})

    return render(request,'seimLiteApp/login.html')

def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        if User.objects.filter(username=username).exists():
            return render(request,'seimLiteApp/signup.html',{'error':'username alresy exists'})
        user=User.objects.create_user(username=username,password=password)
        login(request,user)
        return redirect('dashboard')

    return render(request,'seimLiteApp/signup.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    return render(request,'seimLiteApp/dashboard.html')