# Generated by Django 5.0.3 on 2024-05-16 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0003_alter_leaf_birth_date_alter_leaf_due_date'),
        ('remember', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='leaf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='remembered', to='leaf.leaf'),
        ),
    ]