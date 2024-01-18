from django.db import models

class Type(models.Model):
    type_name = models.CharField(max_length = 50, primary_key = True)    
    #do you wanna do strengths, weaknesses, and immunities bc you might need to have multiple
# Create your models here.

class Pokemon(models.Model):
    dex_num = models.BigAutoField(primary_key = True, editable=False)
    name = models.CharField(max_length=100)
    types = models.JSONField()
    
    base_stats = models.JSONField(default=dict)
    types = models.JSONField(default=dict)
    
    ability = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
