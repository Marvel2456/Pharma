# Generated by Django 4.2 on 2023-05-18 11:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_clientprofile_client_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacist',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=12, null=True),
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=3, default=0, max_digits=12, null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.pharmacist')),
            ],
        ),
    ]