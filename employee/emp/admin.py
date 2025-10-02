from django.contrib import admin

from .models import Position

# Register your models here.
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)