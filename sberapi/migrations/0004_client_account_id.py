# Generated by Django 3.2.9 on 2022-04-28 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sberapi', '0003_alter_clientdata_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='account_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]
