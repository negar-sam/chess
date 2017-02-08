from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Games(models.Model):
	status = models.CharField(max_length=100) 
	user = models.ForeignKey(User)
	
