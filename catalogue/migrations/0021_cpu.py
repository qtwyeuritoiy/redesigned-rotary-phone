# Generated by Django 3.0.10 on 2020-09-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0020_remove_product_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_Name', models.CharField(max_length=255)),
                ('cpu_Mark', models.IntegerField()),
                ('cpu_Rank', models.IntegerField()),
                ('cpu_Value', models.IntegerField()),
                ('cpu_Price', models.IntegerField()),
            ],
        ),
    ]