# Generated by Django 3.0.8 on 2020-08-06 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0008_auto_20200805_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management_type',
            name='Origin',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
