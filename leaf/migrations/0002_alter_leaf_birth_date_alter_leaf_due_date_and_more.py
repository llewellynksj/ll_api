# Generated by Django 5.0.3 on 2024-05-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaf',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='quotation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='leaf',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
