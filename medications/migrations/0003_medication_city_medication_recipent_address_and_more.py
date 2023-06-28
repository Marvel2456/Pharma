# Generated by Django 4.2 on 2023-06-28 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0002_alter_medication_dosage_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='city',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='recipent_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='recipent_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='recipent_phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='state',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='medication',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DELIVERED', 'DELIVERED')], default='PENDING', max_length=20),
        ),
        migrations.AlterField(
            model_name='medication',
            name='dosage_form',
            field=models.CharField(blank=True, choices=[('TABLET', 'TABLET'), ('CAPSULE', 'CAPSULE'), ('SYRUP', 'SYRUP'), ('SOLUTION', 'SOLUTION'), ('EMULSION', 'EMULSION'), ('SUSPENSION', 'SUSPENSION'), ('INHALER', 'INHALER'), ('CREAM', 'CREAM'), ('PASTE', 'PASTE'), ('GEL', 'GEL')], default='TABLET', max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]