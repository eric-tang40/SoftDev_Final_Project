from django.db import models

from pokemon.models import Pokemon

class Trainer(models.Model):
    name = models.CharField(primary_key = True)
    preferred_type = models.CharField()
    badge_name = models.CharField()
    # team  = models.ForeignKey(Pokemon)
    # we meed to wait for novillo documentation for this and types
# Create your models here.
