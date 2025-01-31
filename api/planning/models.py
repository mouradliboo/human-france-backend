from django.db import models
from authentication.models import CustomUser
from users.models import Clients
# Create your models here.
class Ligne(models.Model):
    id = models.BigAutoField(primary_key=True)
    planning  = models.ForeignKey('Planning', on_delete=models.CASCADE, related_name='lignes')
    AGENT_TYPES = [
        ('security', 'Security'),
        ('incendie', 'Incendie'),
    ]
    
    start_date = models.DateField()
    end_date = models.DateField()
  
    agent_type = models.CharField(max_length=10, choices=AGENT_TYPES)
    days = models.CharField(max_length=8)  # Store as a comma-separated string or JSON
    pause = models.IntegerField()
    agent_number = models.IntegerField()
    start_hour = models.TimeField(default="00:00")
    end_hour = models.TimeField(default="00:00")
    start_cutoff = models.DateTimeField(null=True, blank=True)
    end_cutoff = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"Ligne {self.id} ({self.agent_type})"


class Planning(models.Model):
    id = models.BigAutoField(primary_key=True)
    STATE_CHOICES = [
        ('published', 'Published'),
        ('draft', 'Draft'),
     
    ]
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='client')
    site_name = models.CharField(max_length=255)
    state = models.CharField(max_length=15, choices=STATE_CHOICES, default='draft') 

    def __str__(self):
        return f"Planning {self.id} ({self.site_name})"
