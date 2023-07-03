# Generated by Django 4.2 on 2023-07-02 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicationdetail',
            name='medication',
        ),
        migrations.AddField(
            model_name='medication',
            name='medication_details',
            field=models.ManyToManyField(related_name='medications', to='medications.medicationdetail'),
        ),
    ]