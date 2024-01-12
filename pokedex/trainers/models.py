from django.db import models
from pokemon.models import Pokemon

class Trainer(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    preferred_type = models.CharField(max_length = 50)
    badge_name = models.CharField(max_length = 100)
    team  = models.JSONField()
    # we meed to wait for novillo documentation for this and types
# Create your models here.
