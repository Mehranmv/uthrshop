# Generated by Django 4.2.6 on 2023-10-19 16:54

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(unique=True),
        ),
    ]
