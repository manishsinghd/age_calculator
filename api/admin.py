from django.contrib import admin

from .models import calculate


class calculaterAdmin(admin.ModelAdmin):
    list_display=calculate.Displayfields


admin.site.register(calculate, calculaterAdmin)

# Register your models here.
