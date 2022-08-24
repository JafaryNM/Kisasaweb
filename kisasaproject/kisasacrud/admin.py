from django.contrib import admin
from .models import Core
# Register your models here.

@admin.register(Core)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',),}