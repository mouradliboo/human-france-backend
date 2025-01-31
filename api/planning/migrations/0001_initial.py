# Generated by Django 5.1.4 on 2025-01-30 15:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.DateTimeField()),
                ('end_hour', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('agent_type', models.CharField(choices=[('security', 'Security'), ('incendie', 'Incendie')], max_length=10)),
                ('days', models.CharField(max_length=8)),
                ('pause', models.IntegerField()),
                ('agent_number', models.IntegerField()),
                ('horaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='planning.horaire')),
            ],
        ),
        migrations.AddField(
            model_name='horaire',
            name='ligne',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horaires', to='planning.ligne'),
        ),
        migrations.CreateModel(
            name='Planning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plannings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ligne',
            name='planning',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lignes', to='planning.planning'),
        ),
    ]
