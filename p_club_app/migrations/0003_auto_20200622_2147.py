# Generated by Django 3.0.7 on 2020-06-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_club_app', '0002_auto_20200622_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='position_order',
            field=models.IntegerField(default=True, editable=False),
        ),
    ]
