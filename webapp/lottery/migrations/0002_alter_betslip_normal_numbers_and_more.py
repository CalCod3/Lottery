# Generated by Django 5.0.6 on 2024-06-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betslip',
            name='normal_numbers',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='betslip',
            name='star_numbers',
            field=models.TextField(),
        ),
    ]