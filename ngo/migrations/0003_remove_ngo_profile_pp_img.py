# Generated by Django 4.0.4 on 2022-05-22 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0002_alter_ngo_profile_authorized'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ngo_profile',
            name='pp_img',
        ),
    ]
