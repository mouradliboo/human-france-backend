from django.contrib import admin
from .models import Ligne,Conditions,Planning,PlanningAgent,Absences

# Register your models here.
admin.site.register(Planning)
admin.site.register(Ligne)
admin.site.register(Conditions)
admin.site.register(PlanningAgent)
admin.site.register(Absences)

