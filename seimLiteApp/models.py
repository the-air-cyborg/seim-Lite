from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Log(models.Model):
    LEVEL_CHOICES = [
        ("INFO", "Info"),
        ("WARNING","Warning"),
        ("CRITICAL","Critical"),
    ]
    
    STATUS_CHOICES=[
        ("OK","Ok"),
        ("INVESTIGATE","Investigate"),
        ("BLOCKED","Blocked")
    ]

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="logs"
    )
    
    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
    source = models.CharField(max_length=50)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    def __str__(self):
        return f"{self.level} | {self.source}"
    
class Profile(models.Model):
    ROLE_CHOICES=[
        ("ADMIN","Admin"),
        ("ANALYST","Security Analyst"),
        ("VIEWER","Viewer"),
    ]
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="profiles/",blank=True,null=True)
    phone=models.CharField(max_length=15,blank=True)
    address=models.TextField(blank=True)
    role=models.CharField(max_length=20,choices=ROLE_CHOICES,default="VIEWER")
    
    @property
    def is_admin(self):
        return self.role=="ADMIN"
    
    @property
    def is_analyst(self):
        return self.role=="ANALYST"
    
    @property
    def is_viewer(self):
        return self.role=="VIEWER"
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
    