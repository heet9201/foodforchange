# Generated by Django 4.0.4 on 2022-05-23 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0005_posts_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='email',
        ),
        migrations.AddField(
            model_name='posts',
            name='name',
            field=models.CharField(default='null', max_length=30),
        ),
    ]
