from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Register(AbstractUser):
    class Meta:
        verbose_name = "Register"          
        verbose_name_plural = "Register"
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('user',"User"),
    )
    Role=models.CharField(choices=ROLE_CHOICES,default='user')
    def __str__(self):
        return self.username
    
class Search_data(models.Model):
    Name=models.CharField()
    About=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Name

class Students(models.Model):
    name=models.CharField()
    rollno=models.IntegerField()
    city=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    title=models.CharField()
    description=models.TextField()
    scheduled_time=models.DateTimeField()
    is_complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.
