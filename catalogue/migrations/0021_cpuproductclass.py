# Generated by Django 3.0.10 on 2020-09-17 18:27

from django.db import migrations, models
import oscar.models.fields.autoslugfield


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0020_remove_product_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CPUProductClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('slug', oscar.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('requires_shipping', models.BooleanField(default=True, verbose_name='Requires shipping?')),
                ('track_stock', models.BooleanField(default=True, verbose_name='Track stock levels?')),
                ('model_name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('socket_type', models.CharField(max_length=50)),
                ('clock_speed', models.IntegerField()),
                ('core_count', models.IntegerField()),
                ('tdp_rating', models.IntegerField()),
                ('cache_capacity', models.IntegerField()),
                ('options', models.ManyToManyField(blank=True, to='catalogue.Option', verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Product class',
                'verbose_name_plural': 'Product classes',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]