# Generated by Django 4.2 on 2023-05-16 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='coin_value',
        ),
        migrations.AddField(
            model_name='plan',
            name='coin',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
