from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Log,Profile,Project
from .forms import UserRegistrationForm,ProfileRegistrationForm
from django.db import transaction

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("dashboard")
    else:
        form = AuthenticationForm()

    return render(request, "seimLiteApp/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            with transaction.atomic():
                user = user_form.save()

                # profile already exists because of signal
                profile = user.profile
                profile.phone = profile_form.cleaned_data["phone"]
                profile.profile_pic = profile_form.cleaned_data.get("profile_pic")
                profile.save()

            login(request, user)
            return redirect("dashboard")
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()

    return render(request, "seimLiteApp/signup.html", {
        "user_form": user_form,
        "profile_form": profile_form
    })
            


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    return render(request, "seimLiteApp/dashboard.html")


@login_required
def logs_view(request):
    logs = Log.objects.all()

    level = request.GET.get("level")
    status = request.GET.get("status")
    source = request.GET.get("source")

    if level:
        logs = logs.filter(level=level)

    if status:
        logs = logs.filter(status=status)

    if source:
        logs = logs.filter(source__icontains=source)

    logs = logs.order_by("-timestamp")

    return render(request, "seimLiteApp/logs.html", {
        "logs": logs,
        "selected_level": level,
        "selected_status": status,
    })

@login_required
def reports(request):
    return render(request, "seimLiteApp/reports.html")

@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, "seimLiteApp/profile.html", {
        "user":request.user,
        "profile":profile
    })
    
@login_required
def investigations_view(request):
    return render(request,"seimLiteApp/investigations.html")

@login_required
def projects_view(request):
    projects = Project.objects.all()
    return render(request, "seimLiteApp/projects.html", {
        "projects": projects
    })

@login_required
def users_view(request):
    return render(request,"seimLiteApp/users.html")

@login_required
def settings_view(request):
    return render(request,"seimLiteApp/settings.html")

@login_required
def alerts_view(request):
    return render(request,"seimLiteApp/alerts.html")

