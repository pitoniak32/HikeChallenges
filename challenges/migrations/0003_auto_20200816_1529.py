# Generated by Django 3.1 on 2020-08-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_auto_20200816_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mountain',
            name='location_city',
        ),
        migrations.AlterField(
            model_name='mountain',
            name='date_done',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
