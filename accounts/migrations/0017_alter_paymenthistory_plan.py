# Generated by Django 4.2 on 2023-06-01 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_paymenthistory_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.plan'),
        ),
    ]
