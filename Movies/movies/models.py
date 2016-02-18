from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from time import time

def get_upload_file_name(instance, filename):
    return "images/%s_%s" %(str(time()).replace('.','_'),filename.replace(' ', '_'))

class Language(models.Model):
	name = models.TextField()
	def __unicode__(self):
		return str(self.name)

class Genre(models.Model):
	name = models.TextField()
	def __unicode__(self):
		return str(self.name)
	
class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.FileField(upload_to=get_upload_file_name)
	movieLength = models.IntegerField()
	releaseDate = models.DateField()
	language = models.ManyToManyField('Language')
	genre = models.ManyToManyField('Genre')
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return str(self.title)


