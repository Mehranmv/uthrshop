# Generated by Django 4.2.6 on 2023-10-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_slider_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='shortdescription',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
