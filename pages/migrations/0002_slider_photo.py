# Generated by Django 4.2.6 on 2023-10-11 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='photo',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
