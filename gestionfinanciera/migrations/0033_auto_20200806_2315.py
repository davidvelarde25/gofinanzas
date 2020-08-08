# Generated by Django 3.0.9 on 2020-08-07 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0032_auto_20200806_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='Application_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='Date_Of_Receipt',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='Payment_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='client',
            name='Date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='disbursement',
            name='Pay_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Date_Of_Contact',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Result_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Guardianship_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Guardianship_Response_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Reply_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='right_petition',
            name='Send_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='tracing',
            name='Adviser',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='tracing',
            name='Follow_Date',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]