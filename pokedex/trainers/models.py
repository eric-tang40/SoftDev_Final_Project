from django.db import models
from pokemon.models import Pokemon

class Trainer(models.Model):
    name = models.CharField(max_length = 50, primary_key = True)
    preferred_type = models.CharField(max_length = 50)
    badge_name = models.CharField(max_length = 100)
    team  = models.JSONField()
    # we meed to wait for novillo documentation for this and types
# Create your models here.

# Trainer.objects.create(
#     name='Brock',
#     preferred_type='Rock',
#     badge_name='Boulder Badge',
#     team=[]  
# )

# Trainer.objects.create(
#     name='Misty',
#     preferred_type='Water',
#     badge_name='Cascade Badge',
#     team=[]  
# )

# Trainer.objects.create(
#     name='Lieutenant Surge',
#     preferred_type='Electric',
#     badge_name='Thunder Badge',
#     team=[] 
# )

# Trainer.objects.create(
#     name='Erika',
#     preferred_type='Grass',
#     badge_name='Rainbow Badge',
#     team=[] 
# )

# Trainer.objects.create(
#     name='Koga',
#     preferred_type='Poison',
#     badge_name='Soul Badge',
#     team=[] 
# )

# Trainer.objects.create(
#     name='Sabrina',
#     preferred_type='Psychic',
#     badge_name='Marsh Badge',
#     team=[] 
# )

# Trainer.objects.create(
#     name='Giovanni',
#     preferred_type='Ground',
#     badge_name='Earth Badge',
#     team=[] 
# )
