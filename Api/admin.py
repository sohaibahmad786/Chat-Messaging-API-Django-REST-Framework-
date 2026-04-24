from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Register
from .models import Search_data
from .models import Students
from .models import Task
from .models import Booking
from .models import Message

admin.site.register(Message)
admin.site.register(Booking)
admin.site.register(Task)
admin.site.register(Students)
admin.site.register(Search_data)
admin.site.register(Register,UserAdmin)

# Register your models here.
