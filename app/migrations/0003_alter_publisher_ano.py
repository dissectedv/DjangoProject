# Generated by Django 5.2.1 on 2025-05-30 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_author_category_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='ano',
            field=models.IntegerField(),
        ),
    ]
