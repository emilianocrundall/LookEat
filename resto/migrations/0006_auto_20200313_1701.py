# Generated by Django 3.0.4 on 2020-03-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resto', '0005_auto_20200313_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to='covers/%Y/%m/%D/'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='covers/%Y/%m/%D/'),
        ),
    ]
