from django.db import models
from django.contrib import admin
from datetime import date

# Create your models here.
class UserReg(models.Model):
	firstname=models.CharField(max_length=200)
	username=models.CharField(max_length=200)
	email = models.EmailField(max_length=70,unique=True)
	password=models.CharField(max_length=200)
	description=models.CharField(max_length=400)
	location=models.CharField(max_length=400)
	profilepic = models.FileField(upload_to='img')
	def __str__(self):
		return self.username                # __unicode__ on Python 2

class UploadFile(models.Model):
	usernames=models.CharField(max_length=200)
	description=models.CharField(max_length=400)
	category=models.CharField(max_length=200)
	docfile = models.FileField(upload_to='img')
	link=models.URLField()
	imglink=models.CharField(max_length=400)
	
