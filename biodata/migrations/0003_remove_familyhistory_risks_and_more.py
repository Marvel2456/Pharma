# Generated by Django 4.2 on 2023-07-03 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0002_rename_risk_familyhistory_risks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familyhistory',
            name='risks',
        ),
        migrations.RemoveField(
            model_name='medicalhistory',
            name='histories',
        ),
        migrations.RemoveField(
            model_name='patientallergy',
            name='allergies',
        ),
        migrations.AddField(
            model_name='familyhistory',
            name='risks',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicalhistory',
            name='histories',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientallergy',
            name='allergies',
            field=models.TextField(blank=True, null=True),
        ),
    ]