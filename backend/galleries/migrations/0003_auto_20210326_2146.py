# Generated by Django 3.1.7 on 2021-03-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0002_auto_20210326_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='sessionkey',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
