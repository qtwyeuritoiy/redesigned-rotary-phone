# Generated by Django 3.0.10 on 2020-09-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0019_product_video_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='video_url',
        ),
    ]