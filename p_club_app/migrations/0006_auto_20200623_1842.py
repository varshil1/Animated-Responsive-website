# Generated by Django 3.0.7 on 2020-06-23 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_club_app', '0005_auto_20200622_2218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='image',
            new_name='images',
        ),
    ]
