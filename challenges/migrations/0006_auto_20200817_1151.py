# Generated by Django 3.1 on 2020-08-17 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('challenges', '0005_auto_20200816_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mountain',
            name='date_done',
        ),
        migrations.RemoveField(
            model_name='mountain',
            name='users_completed',
        ),
        migrations.AlterField(
            model_name='mountain',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='mountain',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Achivement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_completed', models.DateTimeField(blank=True, default=None, null=True)),
                ('challenge_completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.challenge')),
                ('mountain_completed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.mountain')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
