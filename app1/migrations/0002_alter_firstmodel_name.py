# Generated by Django 3.2 on 2021-04-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstmodel',
            name='name',
            field=models.TextField(default='Name'),
        ),
    ]
