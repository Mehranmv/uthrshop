from django.contrib import admin
from .models import Slider


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
