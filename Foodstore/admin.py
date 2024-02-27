from django.contrib import admin

# Register your models here.

from .models import FoodItem

@admin.register(FoodItem)

class FoodItemAdmin(admin.ModelAdmin):
    list_filter=('vegtype',)
    ordering=('-vitamin','vname',)
    search_fields=('vname',)