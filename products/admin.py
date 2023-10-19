from django.contrib import admin
from .models import Category, Brand, Product, Choices, Pictures, Size
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from mptt.admin import MPTTModelAdmin

class SizeInline(NestedStackedInline):
    model = Size
    extra = 1


class PicturesInline(NestedStackedInline):
    model = Pictures
    extra = 1
    
class ChoiceInline(NestedStackedInline):
    model = Choices
    inlines = [SizeInline, PicturesInline]
    extra = 1




@admin.register(Product)
class ProductAdmin(NestedModelAdmin):
    list_display = ('name', 'available', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ChoiceInline]

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
