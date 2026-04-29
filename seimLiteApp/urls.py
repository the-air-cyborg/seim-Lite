from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.login_view,name='login'),
    path('signup/',views.signup_view,name='signup'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logs/',views.logs_view,name='logs'),
    path("reports/",views.reports, name="reports"),
    path("profile/",views.profile_view, name="profile"),
    path("investigations/",views.investigations_view, name="investigations"),
    path("projects/",views.projects_view, name="projects"),
    path("users/",views.users_view, name="users"),
    path("settings/",views.settings_view, name="settings"),
    path("alerts/",views.alerts_view, name="alerts"),
    path("projects/<int:project_id>/", views.project_detail, name="project_detail"),
    path("logs/<int:log_id>/investigate/", views.investigate_log, name="investigate_log")
]