# Generated by Django 4.1.4 on 2023-04-26 06:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_rename_idreceta_ingredientereceta_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientereceta',
            old_name='nombre',
            new_name='idReceta',
        ),
    ]