# Generated by Django 5.2 on 2025-04-19 04:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=51)),
                ('last_name', models.CharField(blank=True, max_length=51)),
                ('phone', models.CharField(max_length=51)),
                ('email', models.EmailField(blank=True, max_length=255)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(blank=True)),
            ],
        ),
    ]
