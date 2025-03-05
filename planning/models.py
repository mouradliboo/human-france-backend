from django.db import models
from authentication.models import CustomUser
from users.models import Clients,AgentProfile
from django.db.models.signals import pre_save
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

import datetime
class Ligne(models.Model):
    id = models.BigAutoField(primary_key=True)
    planning  = models.ForeignKey('Planning', on_delete=models.CASCADE, related_name='lignes')


    AGENT_TYPES = [
        ('agent_securite_confirme', 'Agent de sécurité confirmé'),
        ('agent_securite_magasin_prevol', 'Agent de sécurité magasin prévol'),
        ('agent_securite_filtrage', 'Agent de sécurité filtrage'),
        ('agent_securite_qualifie', 'Agent de sécurité qualifié'),
        ('conducteur_chien', 'Conducteur de chien'),
        ('agent_securite_SSIAP1', 'Agent de sécurité SSIAP1'),
        ('chef_equipe_SSIAP2', 'Chef d’équipe SSIAP2'),
        ('chef_site_SSIAP3', 'Chef de site SSIAP3'),
        ('agent_mobile', 'Agent mobile'),
        ('agent_rondier', 'Agent rondier'),
        ('chef_de_site', 'Chef de site'),
        ('adjoint_chef_site', 'Adjoint chef de site'),
        ('chef_equipe', 'Chef d’équipe'),
        ('chef_poste', 'Chef de poste'),
        ('operateur_video_sct1', 'Opérateur vidéo SCT 1'),
        ('operateur_video_sct2', 'Opérateur vidéo SCT 2'),
    ]





    
    start_date = models.DateField()
    end_date = models.DateField()
    days_needs = models.CharField(max_length=255,null=True, blank=True)

    
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


@receiver(pre_save, sender=Ligne)
def set_days_needs(sender, instance, **kwargs):
    if instance.days_needs is None:
        days_needs= list(instance.month_days)
        days_needs = [str(instance.agent_number) if x=="y" else "0" for x in days_needs]
        instance.days_needs= ",".join(days_needs)
        print(instance.days_needs)
        
        

  


class Conditions(models.Model):
    SALARY_TYPES = [
        ('net', 'Net'),
        ('brute', 'Brute'),
    ]
    
    description = models.TextField()
    hour_salary = models.FloatField()
    salary_type = models.CharField(max_length=100, choices=SALARY_TYPES)
    minimal_hours = models.IntegerField()
    maximal_hours = models.IntegerField(null=True, blank=True)
    tenues = models.CharField(max_length=255,null=True, blank=True)
    languages = models.CharField(max_length=255)
    experience = models.JSONField(null=True, blank=True)
    def __str__(self):
        return f"Conditions {self.id}"



class Planning(models.Model):
    id = models.BigAutoField(primary_key=True)
    STATE_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
        ('archived', 'Archived'),
        ('en_cours', 'En cours'),
     
    ]
    total_hours = models.IntegerField(default=0)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='client')
    site_name = models.CharField(max_length=255,null=True, blank=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='draft') 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    start_planning_date = models.DateField(default ="2025-02-01")
    conditions = models.OneToOneField(Conditions, related_name='condition',null=True, blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"Planning {self.id} ({self.site_name})"




class PlanningAgent(models.Model):
    Status_Values=[
        ('accepted', 'Accepted'),
        ('refused', 'Refused'),
        ('pending', 'Pending'),
    ]
    id = models.BigAutoField(primary_key=True)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='planning')
    agent = models.ForeignKey(AgentProfile, on_delete=models.CASCADE, related_name='agent')
    status = models.CharField(max_length=20, choices=Status_Values, default='pending')
    demande = models.JSONField(null=True, blank=True)
    position = models.JSONField(null=True, blank=True)
    agent_function = models.CharField(max_length=255)
    nbr_heure = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    def __str__(self):
        return f"PlanningAgent {self.id} ({self.agent})"
    class Meta:
        unique_together = ('planning', 'agent')  # Old method (still works)
        # OR (Preferred for new Django versions)
        constraints = [
            models.UniqueConstraint(fields=['planning', 'agent'], name='unique_planning_agent')
        ]
        
        

    