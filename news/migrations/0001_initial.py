# Generated by Django 3.1.2 on 2020-10-30 17:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_es', models.CharField(max_length=255, null=True)),
                ('title_ca', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('title_fr', models.CharField(max_length=255, null=True)),
                ('text', models.TextField()),
                ('text_es', models.TextField(null=True)),
                ('text_ca', models.TextField(null=True)),
                ('text_en', models.TextField(null=True)),
                ('text_fr', models.TextField(null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
