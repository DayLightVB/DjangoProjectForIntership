# Generated by Django 3.1.1 on 2021-01-03 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20210103_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/polls/img/'),
        ),
    ]
