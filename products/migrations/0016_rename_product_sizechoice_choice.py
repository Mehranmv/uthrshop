# Generated by Django 4.2.6 on 2023-10-17 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_sizechoice_product_alter_sizechoice_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sizechoice',
            old_name='product',
            new_name='choice',
        ),
    ]
