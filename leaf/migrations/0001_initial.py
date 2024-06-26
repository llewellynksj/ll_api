# Generated by Django 5.0.3 on 2024-05-16 11:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('memory', models.TextField()),
                ('parent1', models.CharField(max_length=100)),
                ('parent2', models.CharField(blank=True, max_length=100)),
                ('due_date', models.DateField()),
                ('birth_date', models.DateField()),
                ('weight', models.IntegerField()),
                ('quotation', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='../default_profile', upload_to='images/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
