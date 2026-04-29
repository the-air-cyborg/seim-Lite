from django.contrib import admin
from django.shortcuts import render
from .models import Project,Log,Profile
from django.contrib.auth.decorators import login_required

admin.site.register(Project)
admin.site.register(Profile)

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display=("timestamp","level","source","status")
    list_filter=("level","status","source")
    search_fields=("message",)
    
@login_required
def account_view(request):
    profile = request.user.profile
    return render(request, "seimLiteApp/account.html", {
        "profile": profile
    })
