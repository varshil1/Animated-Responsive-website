# Generated by Django 3.0.7 on 2020-06-23 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_club_app', '0006_auto_20200623_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='desc',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='about_us',
            name='objectives',
            field=models.CharField(max_length=2000),
        ),
    ]
