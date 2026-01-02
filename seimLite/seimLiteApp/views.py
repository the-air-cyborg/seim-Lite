from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "seimLiteApp/login.html", {
        "form": form
    })


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