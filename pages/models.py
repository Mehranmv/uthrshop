# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _
# Locale Imports
from utils import AbstractDateTime
# Third Party imports
from ckeditor.fields import RichTextField
from mptt.models import MPTTModel, TreeForeignKey


class Slider(AbstractDateTime):
    title = models.CharField(max_length=256)
    shortdescription = models.CharField(max_length=50)
    description = RichTextField()
    link = models.URLField()
    photo = models.ImageField(
        upload_to="post/",
    )

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")
        ordering = ("updated",)

    def __str__(self):
        return f'{self.title} - {self.description}'


class Menu(MPTTModel):
    title = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(
        unique=True,
    )
    link = models.URLField()
    parent = TreeForeignKey(
        'self', 
        on_delete=models.CASCADE,
        null=True, 
        blank=True, 
        related_name='children'
        )

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def __str__(self):
        return self.title
