from django.db import models

# Create your models here.

class Users(models.Model):
	mail = models.CharField( max_length=50 , primary_key=True)
	name = models.CharField( max_length=50 )
	password = models.CharField( max_length=30 )
class Games(models.Model):
	status = models.CharField(max_length=100) 
	user = models.ForeignKey(Users)
	