# Generated by Django 2.2 on 2019-12-20 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_in', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]
