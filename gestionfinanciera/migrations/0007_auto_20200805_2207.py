# Generated by Django 3.0.8 on 2020-08-06 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0006_auto_20200805_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management_type',
            name='Campaign',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
