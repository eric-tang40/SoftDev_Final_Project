from django.db import models

class Type(models.Model):
    type_name = models.CharField(max_length = 50, primary_key = True)    
    #do you wanna do strengths, weaknesses, and immunities bc you might need to have multiple
# Create your models here.

class Pokemon(models.Model):
    dex_num = models.SmallIntegerField(primary_key = True)
    type = models.ManyToManyField(Type)
    name = models.CharField(max_length = 50)
    
    hp = models.SmallIntegerField()
    attack = models.SmallIntegerField()
    sp_atk = models.SmallIntegerField()
    defense = models.SmallIntegerField()
    sp_def = models.SmallIntegerField()
    speed = models.SmallIntegerField()
    ability = models.CharField(max_length = 50)
