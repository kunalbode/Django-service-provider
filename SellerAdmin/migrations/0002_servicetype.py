# Generated by Django 2.2 on 2019-11-18 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SellerAdmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
    ]
