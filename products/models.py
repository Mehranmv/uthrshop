from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from enum import Enum
from ckeditor.fields import RichTextField


class Available(Enum):
    IN_STOCK = '1'
    OUT_OF_STOCK = '0'


class Sizes(Enum):
    L = 'L'
    X = 'X'
    XL = 'XL'


class Category(MPTTModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    is_sub_category = models.BooleanField(
        default=False,
        verbose_name='Sub Category'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title


class Brand(models.Model):
    name = models.CharField(
        max_length=100
    )
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=256
    )
    slug = models.SlugField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        upload_to='product/photos'
    )
    price = models.FloatField()
    available = models.CharField(
        choices=[(status.value, status.name) for status in Available],
        default=Available.IN_STOCK.value,
    )
    short_description = models.CharField(
        max_length=150
    )
    description = RichTextField()
    tags = RichTextField()
    additional_information = RichTextField(
        verbose_name='Additional Information'
    )


# inlines



class Choices(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    color_name = models.CharField(
        max_length=50
    )
    color_code = models.CharField(
        max_length=20,
        verbose_name='Color Code',
        help_text='#f456a'
    )
    # size = models.CharField(
    #     choices=[(size.value, size.name) for size in Sizes],
    # )
    price = models.FloatField(
        blank=True,
        null=True,
        help_text='blank to use Base price'
    )
    inventory = models.IntegerField()


class Size(models.Model):
    choice = models.ForeignKey(
        Choices,
        on_delete=models.CASCADE,
    )
    size = models.CharField(
        max_length=200,
    )


class Pictures(models.Model):
    choice = models.ForeignKey(
        Choices,
        on_delete=models.CASCADE,
    )
    picture = models.ImageField(upload_to='product/photos')

    def __str__(self):
        return self.picture.url
