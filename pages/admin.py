from django.contrib import admin
from .models import Slider, Menu
from mptt.admin import DraggableMPTTAdmin


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'updated'
    )
    list_filter = ('updated',)
    search_fields = (
        'title',
        'description',
    )


@admin.register(Menu)
class MenuAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {
        'slug': ("title",)
    }
