# Generated by Django 4.2.1 on 2023-07-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expanse',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
