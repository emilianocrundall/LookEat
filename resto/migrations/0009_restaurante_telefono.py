# Generated by Django 3.0.4 on 2020-03-25 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0008_restaurante_imagen_principal'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='telefono',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
