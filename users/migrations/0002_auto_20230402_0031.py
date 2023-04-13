# Generated by Django 3.2.16 on 2023-04-01 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='patent_end',
            field=models.DateField(blank=True, null=True, verbose_name='Срок окончания патента'),
        ),
        migrations.AlterField(
            model_name='user',
            name='patent_start',
            field=models.DateField(blank=True, null=True, verbose_name='Срок действия патента'),
        ),
    ]
