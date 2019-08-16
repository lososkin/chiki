from django.db import models

# Create your models here.

class Chika(models.Model):
	"""docstring for ClassName"""
	vk_link = models.CharField(max_length=250)
	photo_link = models.CharField(max_length=250)
	likes = models.IntegerField()