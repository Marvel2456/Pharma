# Generated by Django 4.2 on 2023-06-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biodata', '0006_alter_medicalrecord_height_and_more'),
        ('chat', '0003_chatroom_allergy_chatroom_fam_history_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='allergy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.patientallergy'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='fam_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.familyhistory'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='med_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.medicalhistory'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='med_records',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biodata.medicalrecord'),
        ),
    ]