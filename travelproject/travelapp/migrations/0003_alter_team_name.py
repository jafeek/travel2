# Generated by Django 3.2.18 on 2023-08-10 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]
