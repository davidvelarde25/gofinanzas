# Generated by Django 3.0.9 on 2020-08-07 04:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestionfinanciera', '0036_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actual_state',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Advisor_Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Identification', models.DecimalField(decimal_places=0, max_digits=20, null=True)),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Address', models.CharField(max_length=250)),
                ('City', models.CharField(blank=True, max_length=250)),
                ('Cell_Phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('Phone', models.IntegerField(blank=True, null=True)),
                ('Date_of_birth', models.DateField(blank=True, default=datetime.date.today)),
                ('Stratum', models.IntegerField(blank=True, null=True)),
                ('Neighborhood', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Referrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Management_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Origin', models.CharField(max_length=250, null=True)),
                ('Campaign', models.CharField(max_length=250)),
                ('Campus', models.CharField(max_length=250, null=True)),
                ('Outcome', models.CharField(max_length=250, null=True)),
                ('Result_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Date_Of_Contact', models.DateField(blank=True, default=datetime.date.today)),
                ('Actual_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Actual_state')),
                ('Advisor_Records', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Advisor_Records')),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Client')),
                ('Customer_Referrer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Customer_Referrer')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Tracing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=2000)),
                ('Follow_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Adviser', models.DateField(blank=True, default=datetime.date.today)),
                ('Management_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Right_Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Application', models.CharField(max_length=250)),
                ('Send_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Filed_Number', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Reply_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Process_state', models.CharField(max_length=250, null=True)),
                ('Reply', models.CharField(max_length=600, null=True)),
                ('Guardianship_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Court', models.CharField(max_length=250, null=True)),
                ('Guardianship_Response_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Observation', models.CharField(max_length=1000, null=True)),
                ('Management_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Address', models.CharField(max_length=250, null=True)),
                ('Labor_Company', models.CharField(max_length=250, null=True)),
                ('City', models.CharField(max_length=250, null=True)),
                ('Relationship', models.CharField(max_length=250, null=True)),
                ('Cell_Phone', models.DecimalField(decimal_places=0, max_digits=20)),
                ('Phone', models.IntegerField(null=True)),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gestionfinanciera.Rol')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payroll_Company', models.CharField(max_length=250)),
                ('Payroll_Type', models.CharField(max_length=250)),
                ('Salary_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Permanent_Income', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Social_Security', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Law_Applies', models.CharField(max_length=250)),
                ('Permanent_Discounts', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Non_Concellable_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Payment_Capacity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Contract_Type', models.CharField(max_length=250)),
                ('Bonding_Date', models.CharField(max_length=250)),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_Obligation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Obligation_Number', models.CharField(max_length=250)),
                ('Type', models.CharField(max_length=250)),
                ('Entity_Obligation', models.CharField(max_length=250)),
                ('State', models.CharField(max_length=250)),
                ('Outstanding_Fees', models.IntegerField(null=True)),
                ('Quota_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Future_Value_Portfolio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Certified_Value_Obligation', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Saving_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Buyer', models.CharField(max_length=250, null=True)),
                ('Default_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Default_Time', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Buy_Mora_Portfolio', models.CharField(max_length=250, null=True)),
                ('Reported_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Offer_Value_To_Entity', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Negotiated_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Negotiated_With', models.CharField(max_length=250, null=True)),
                ('Client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Client')),
                ('Management_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_value', models.CharField(max_length=250, null=True)),
                ('Pay_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Banking_Entity', models.CharField(max_length=250, null=True)),
                ('Disbursement_Amount', models.CharField(max_length=250, null=True)),
                ('Odds_Number', models.CharField(max_length=250, null=True)),
                ('Disbursement_Value', models.CharField(max_length=250, null=True)),
                ('Adviser', models.CharField(max_length=250, null=True)),
                ('State', models.CharField(max_length=250, null=True)),
                ('Management_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=250)),
                ('Application_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Date_Of_Receipt', models.DateField(blank=True, default=datetime.date.today)),
                ('Certificate_Days', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Certified_Value', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Payment_Date', models.DateField(blank=True, default=datetime.date.today)),
                ('Financial_Obligation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Financial_Obligation')),
            ],
        ),
        migrations.CreateModel(
            name='Bank_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_Type', models.CharField(max_length=250, null=True)),
                ('Number', models.DecimalField(decimal_places=2, max_digits=15)),
                ('Bank', models.CharField(max_length=250, null=True)),
                ('State', models.CharField(max_length=250, null=True)),
                ('Management_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Management_type')),
            ],
        ),
    ]
