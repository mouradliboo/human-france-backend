from django.db import models
from authentication.models import CustomUser
from django.utils.timezone import now
# Create your models here.
class AgentProfile(models.Model):
   
    DRIVER_LICENCE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('N', 'N'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved')
        ,('refused','Refused'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="agent_profile")
    photo_identity = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    nss = models.CharField(max_length=50, unique=True)
    card_number_pro = models.CharField(max_length=50, unique=True)
    security_card_photo = models.CharField(max_length=255, null=True, blank=True)
    nub = models.CharField(max_length=10, null=True, blank=True)
    agent_function = models.TextField(null=True, blank=True)
    driver_licence_type = models.CharField(max_length=2, choices=DRIVER_LICENCE_CHOICES, default='N')
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=20)
    ville = models.CharField(max_length=100,null=True,blank=True,default="paris")
    diplomes = models.JSONField(null=True, blank=True)
    experience = models.JSONField(null=True, blank=True)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100,null=True, blank=True)
    nationality = models.CharField(max_length=100,null=True, blank=True)
    tenues = models.CharField(max_length=255, null=True, blank=True)
    languages = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending') 

    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Agent Profile for {self.user.first_name} {self.user.last_name}"
