# Generated by Django 2.2 on 2019-11-19 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SellerAdmin', '0004_subservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='SellerAdmin.SubService'),
            preserve_default=False,
        ),
    ]
