# Generated by Django 4.0.5 on 2022-06-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empnum', models.IntegerField()),
                ('empname', models.CharField(max_length=30)),
                ('empsalary', models.IntegerField()),
                ('empAddress', models.CharField(max_length=200)),
            ],
        ),
    ]