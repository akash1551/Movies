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
	language = models.IntegerField()
	genre = models.IntegerField()

class Language:
	English = 0
	Hindi = 1
	Marathi = 2
	Tamil = 3

	LANGUAGECHOICES = ((English,"English"),(Hindi,"Hindi"),(Marathi,"Marathi"),(Tamil,"Tamil"))

class Genre:
	All = 0
	Horror = 1
	Indian = 2
	Thriller = 3
	Award_Winning = 4
	Animation = 5
	Romance = 6
	Comedy = 7
	Famous_Directors = 8
	Fantasy = 9
	Experimental = 10
	Bed_Time_Stories = 11
	Dark = 12
	Drama = 13
	Short_Doc = 14
	Oscar_Winning = 15
	Family = 16
	Surreal = 17
	Space = 18

	GENRECHOICES = ((All,"All"),(Horror,"Horror"),(Indian,"Indian"),(Thriller,"Thriller"),
		(Award_Winning,"Award Winning"),(Animation,"Animation"),(Romance,"Romance"),(Comedy,"Comedy"),
		(Famous_Directors,"Famous Directors"),(Fantasy,"Fantasy"),(Experimental,"Experimental"),(Bed_Time_Stories,"Bed Time Stories"),
		(Dark,"Dark"),(Drama,"Drama"),(Short_Doc,"Short Doc"),(Oscar_Winning,"Oscar Winning"),
		(Family,"Family"),(Surreal,"Surreal"),(Space,"Space"))

class Relationship(models.Model):
	taxonomyId = models.ForeignKey('Category')
	movieId = models.ForeignKey('Movie')
	