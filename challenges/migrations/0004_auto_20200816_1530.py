# Generated by Django 3.1 on 2020-08-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_auto_20200816_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountain',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='longitude',
            field=models.FloatField(),
        ),
    ]