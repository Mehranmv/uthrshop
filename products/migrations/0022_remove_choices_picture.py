# Generated by Django 4.2.6 on 2023-10-18 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_remove_pictures_product_pictures_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choices',
            name='picture',
        ),
    ]
