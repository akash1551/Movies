from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from time import time

def get_upload_file_name(instance, filename):
    return "images/%s_%s" %(str(time()).replace('.','_'),filename.replace(' ', '_'))

class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	image = models.FileField(upload_to=get_upload_file_name)
	movieLength = models.IntegerField()
	releaseDate = models.DateField("%b %d %Y")

class Category(models.Model):
