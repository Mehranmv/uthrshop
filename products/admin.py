from django.contrib import admin
from .models import Category, Brand, Product, Choices, Pictures
from mptt.admin import MPTTModelAdmin


class PicturesInline(admin.TabularInline):
    model = Pictures


class ChoiceInline(admin.StackedInline):
    model = Choices


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'available', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ChoiceInline, PicturesInline]

    fieldsets = [
        (
            'Title and Slug',
            {
                'fields': ('name', 'slug'),
            }
        ),
        (
            'Base Photo',
            {
                'fields': ('photo',)
            }
        ),
        (
            'Price and Availability',
            {
                'fields': ('price', 'available')
            }
        ),
        (
            'Category & Brand',
            {
                'fields': ('category', 'brand')
            }
        ),
        (
            'Descriptions',
            {
                'fields': ('short_description', 'description')
            }
        ),
        (
            'tags',
            {
                'fields': ("tags",)
            }
        ),
        (
            'Additional Information',
            {
                'fields': ("additional_information",),
            }
        )
    ]


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ('title', 'parent')
    search_fields = ('title',)
    prepopulated_fields = {
        "slug": ('title',)
    }


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
