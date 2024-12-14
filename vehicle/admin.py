from django.contrib import admin

# Register your models here.
from .models import Mechanic


class MechanicAdmin(admin.ModelAdmin):
    list_display = ("user","profile_pic","skill")



admin.site.register(Mechanic,MechanicAdmin)