# Generated by Django 4.2.1 on 2023-07-18 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0002_alter_expanse_desc_alter_income_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='firs_name',
            new_name='first_name',
        ),
    ]
