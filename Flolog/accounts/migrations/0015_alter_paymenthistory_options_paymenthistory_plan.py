# Generated by Django 4.2 on 2023-06-01 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_paymenthistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paymenthistory',
            options={'verbose_name_plural': 'payment histories'},
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='plan',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]