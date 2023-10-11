# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _
# Locale Imports
from utils import AbstractDateTime


class Slider(AbstractDateTime):
    title = models.CharField(max_length=256)
    description = models.TextField()
    link = models.URLField()
    photo = models.ImageField()

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Slides")
        ordering = ("title",)

    def __str__(self):
        return f'{self.title} - {self.description}'
