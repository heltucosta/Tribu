# Generated by Django 2.0.3 on 2018-04-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compensacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compensations',
            name='date_end',
            field=models.DateField(verbose_name='Data fim'),
        ),
        migrations.AlterField(
            model_name='compensations',
            name='date_start',
            field=models.DateField(verbose_name='Data de início'),
        ),
    ]