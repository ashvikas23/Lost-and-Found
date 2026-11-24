from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'date', 'user')
    list_filter = ('category', 'date')
    search_fields = ('title', 'location', 'description')

