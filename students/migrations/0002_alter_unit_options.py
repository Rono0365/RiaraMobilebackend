# Generated by Django 3.2.9 on 2021-11-27 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unit',
            options={'ordering': ['time_taught']},
        ),
    ]
