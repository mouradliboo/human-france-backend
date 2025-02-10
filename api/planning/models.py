from django.db import models
from authentication.models import CustomUser
from users.models import Clients
# Create your models here.

import datetime
class Ligne(models.Model):
    id = models.BigAutoField(primary_key=True)
    planning  = models.ForeignKey('Planning', on_delete=models.CASCADE, related_name='lignes')
    AGENT_TYPES = [

    ('Agent de sécurité confirmé', 'agent_securite_confirme'),
    ('Agent de sécurité magasin prévol', 'agent_securite_magasin_prevol'),
    ('Agent de sécurité filtrage', 'agent_securite_filtrage'),
    ('Agent de sécurité qualifié', 'agent_securite_qualifie'),
    ('Conducteur de chien', 'conducteur_chien'),
    ('Agent de sécurité SSIAP1', 'agent_securite_SSIAP1'),
    ('Agent de sécurité SSIAP2', 'agent_securite_SSIAP2'),
    ('Agent de sécurité SSIAP3', 'agent_securite_SSIAP3'),
    ('chef_de_site', 'Chef de site'),
    ('adjoint_chef_site', 'Adjoint chef de site'),
    ('chef_equipe', 'Chef d’équipe'),
    ('Agent mobile', 'agent_mobile'),
    ('chef_poste', 'chef_poste'),
    ('operateur_video_sct1', 'Opérateur vidéo SCT 1'),
    ('operateur_video_sct2', 'Opérateur vidéo SCT 2'),
    ('Agent rondier', 'agent_rondier'),
]
  


    
    start_date = models.DateField()
    end_date = models.DateField()
    
    agent_type = models.CharField(max_length=100, choices=AGENT_TYPES)
    week_days = models.CharField(max_length=20)  # Store as a comma-separated string or JSON
    month_days = models.CharField(max_length=60)
    selected_days = models.CharField(max_length=100,null=True, blank=True)
    pause = models.IntegerField()
    isPausePaid = models.BooleanField(default=False)
    
    agent_number = models.IntegerField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    start_cutoff = models.TimeField(null=True, blank=True,default=None)
    end_cutoff = models.TimeField(null=True, blank=True,default=None)
   

    def __str__(self):
        return f"Ligne {self.id} ({self.agent_type})"


class Planning(models.Model):
    id = models.BigAutoField(primary_key=True)
    STATE_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
     
    ]
    total_hours = models.IntegerField(default=0)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='client')
    site_name = models.CharField(max_length=255)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='draft') 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    start_planning_date = models.DateField(default ="2025-02-01")

    def __str__(self):
        return f"Planning {self.id} ({self.site_name})"
