# Generated by Django 3.2.5 on 2021-08-11 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(max_length=20),
        ),
    ]
