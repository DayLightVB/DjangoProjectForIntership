# Generated by Django 3.1.1 on 2020-12-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='color',
            field=models.CharField(max_length=100, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='condition',
            field=models.CharField(max_length=100, verbose_name='Condition'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='product_type',
            field=models.CharField(max_length=100, verbose_name='Type'),
        ),
    ]
