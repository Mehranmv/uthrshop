from django.db import models


# class Category(models.Model):
#     title = models.CharField(max_length=100)
#     slug = models.SlugField()
#     parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='children')
#
#     class MPTTMeta:
#         pass
#
#     class Meta:
#         pass
#
#     def __str__(self):
#         return self.title
