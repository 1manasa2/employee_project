# Generated by Django 4.0.5 on 2022-06-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grocery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('qty', models.IntegerField()),
                ('Rpu', models.FloatField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
