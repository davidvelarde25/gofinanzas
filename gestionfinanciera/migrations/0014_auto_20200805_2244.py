# Generated by Django 3.0.8 on 2020-08-06 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0013_management_type_customer_referrer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='management_type',
            name='Customer_Referrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Customer_Referrer'),
        ),
    ]
