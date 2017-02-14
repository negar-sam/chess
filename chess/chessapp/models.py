from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Games(models.Model):
	status = models.CharField(max_length=100,default="rnbqkbnr/pppppppp/......../......../......../......../PPPPPPPP/RNBQKBNR//") 
	user = models.OneToOneField(User, related_name="Game", null=True, blank=True)
	 
