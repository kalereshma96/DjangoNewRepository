# Generated by Django 2.0.3 on 2018-12-15 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20181215_0921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='emp_id',
            new_name='user_id',
        ),
    ]
