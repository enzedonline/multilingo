# Generated by Django 3.1.2 on 2020-11-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201106_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(max_length=200, null=True, verbose_name='Page URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug_ca',
            field=models.SlugField(max_length=200, null=True, verbose_name='Page URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug_en',
            field=models.SlugField(max_length=200, null=True, verbose_name='Page URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug_es',
            field=models.SlugField(max_length=200, null=True, verbose_name='Page URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='slug_fr',
            field=models.SlugField(max_length=200, null=True, verbose_name='Page URL'),
        ),
    ]
