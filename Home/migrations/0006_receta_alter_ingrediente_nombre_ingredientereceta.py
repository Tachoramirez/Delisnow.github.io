# Generated by Django 4.1.4 on 2023-04-26 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_ingrediente_producto_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=250)),
                ('tiempoPrep', models.IntegerField()),
                ('instrucciones', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='nombre',
            field=models.TextField(max_length=50),
        ),
        migrations.CreateModel(
            name='IngredienteReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(max_length=5)),
                ('unidad', models.TextField(max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('idIngrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.ingrediente')),
                ('idReceta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.receta')),
            ],
            options={
                'verbose_name': 'Detalle receta',
                'verbose_name_plural': 'Detalle recetas',
            },
        ),
    ]