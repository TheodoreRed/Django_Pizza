# Generated by Django 4.1.3 on 2022-12-21 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default='2022-12-21 12:34:56'),
            preserve_default=False,
        ),
    ]
