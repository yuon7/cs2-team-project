# Generated by Django 5.0 on 2024-01-05 00:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('price_range', models.CharField(max_length=50)),
                ('like', models.IntegerField(default=0)),
                ('slug', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('posted_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodApp.restaurant')),
            ],
        ),
    ]