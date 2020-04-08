# Generated by Django 3.0.4 on 2020-03-11 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurante',
            name='imagen',
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='platos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='resto.Plato'),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='covers/%Y/%m/%D/')),
                ('restaurante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resto.Restaurante')),
            ],
        ),
    ]
