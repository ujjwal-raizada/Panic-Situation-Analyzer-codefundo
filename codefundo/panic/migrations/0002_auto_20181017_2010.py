# Generated by Django 2.1.2 on 2018-10-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=10),
        ),
    ]
