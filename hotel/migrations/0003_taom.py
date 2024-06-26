# Generated by Django 5.0.6 on 2024-05-19 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_product_malumot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taom', to='hotel.product')),
            ],
        ),
    ]
