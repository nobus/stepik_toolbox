from django.contrib import admin
from .models import TheCat

# Register your models here.
class TheCatAdmin(admin.ModelAdmin):
    pass

admin.site.register(TheCat, TheCatAdmin)
