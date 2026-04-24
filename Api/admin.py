from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Message

admin.site.register(Message)
admin.site.register(Register,UserAdmin)

# Register your models here.
