# Generated by Django 4.1.3 on 2022-12-22 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_pizza_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='state',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
