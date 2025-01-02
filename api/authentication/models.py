from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now

from django.contrib.auth.models import  AbstractUser
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('agent', 'Agent'),
        ('admin', 'Admin'),
        ('responsable', 'Responsable'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
    ]

    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='agent')
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='agent')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.role}"


