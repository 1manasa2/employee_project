# Generated by Django 4.0.5 on 2022-06-26 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roombook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='Roomtype',
            field=models.CharField(choices=[('1', 'Standard'), ('2', 'Classic'), ('3', 'Deluxe')], max_length=200),
        ),
    ]
