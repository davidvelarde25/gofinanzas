# Generated by Django 3.0.8 on 2020-08-06 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionfinanciera', '0005_auto_20200805_2058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Campus',
        ),
        migrations.DeleteModel(
            name='Outcome',
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Actual_state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionfinanciera.Actual_state'),
        ),
        migrations.AlterField(
            model_name='management_type',
            name='Origin',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.DeleteModel(
            name='Origin',
        ),
    ]
