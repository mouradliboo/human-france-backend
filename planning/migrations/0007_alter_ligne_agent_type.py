# Generated by Django 5.1.4 on 2025-02-02 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0006_alter_ligne_agent_type_alter_planning_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ligne',
            name='agent_type',
            field=models.CharField(choices=[('agent_securite_confirme', 'Agent de sécurité confirmé'), ('agent_securite_magasin_prevol', 'Agent de sécurité magasin prévol'), ('agent_securite_filtrage', 'Agent de sécurité filtrage'), ('agent_securite_qualifie', 'Agent de sécurité qualifié'), ('conducteur_chien', 'Conducteur de chien'), ('agent_securite_SSIAP1', 'Agent de sécurité SSIAP1'), ('agent_securite_SSIAP2', 'Agent de sécurité SSIAP2'), ('agent_securite_SSIAP3', 'Agent de sécurité SSIAP3'), ('Chef de site', 'chef_de_site'), ('Adjoint chef de site', 'adjoint_chef_site'), ('Chef d’équipe', 'chef_equipe'), ('agent_mobile', 'Agent mobile'), ('chef_poste', 'chef_poste'), ('Opérateur vidéo SCT 1', 'operateur_video_sct1'), ('Opérateur vidéo SCT 2', 'operateur_video_sct2'), ('agent_rondier', 'Agent rondier')], max_length=100),
        ),
    ]
