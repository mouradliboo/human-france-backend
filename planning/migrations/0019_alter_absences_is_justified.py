# Generated by Django 4.2.10 on 2025-04-11 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0018_absences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absences',
            name='is_justified',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
