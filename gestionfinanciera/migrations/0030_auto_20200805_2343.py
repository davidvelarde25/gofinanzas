# Generated by Django 3.0.8 on 2020-08-06 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0029_auto_20200805_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='Address',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
