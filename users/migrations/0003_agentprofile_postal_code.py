# Generated by Django 5.1.4 on 2025-01-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_agentprofile_nationality'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentprofile',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
