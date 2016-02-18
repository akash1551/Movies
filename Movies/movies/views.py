from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView 
from models import Movie,Language,Genre
import json, datetime
from django.shortcuts import render

def landing_page(request):
	return render_to_response('landing_page.html')

def get_language_and_genre(request):
	languageObj = Language.objects.all()
	genreObj = Genre.objects.all()
	languageList = []
	genreList = []
	for i in languageObj:
		obj = {"id":i.id,"name":i.name, "tag": "LANGUAGE"}
		languageList.append(obj)
	for i in genreObj:
		obj = {"id":i.id,"name":i.name, "tag": "GENRE"}
		genreList.append(obj)
	return HttpResponse(json.dumps({"languageList":languageList,"genreList":genreList,"status":True}), content_type="application/json")
	

def show_all_movies(request):
	movie=Movie.objects.all()
	movieList=[]
	for i in movie:
		date=int(i.date.strftime("%s")) * 1000
		obj={"imageUrl": 'Media/'+str(i.image),"releaseDate": releaseDate,"title": i.title,"movieLength": i.movieLength,"description": i.decription}
		movieList.append(obj)
	return HttpResponse(json.dumps({"movieList": movieList}), content_type="application/json")

def save_movie_data(request):
	if request.POST:
		imageName=request.FILES['imageName']
		releaseDate=request.POST['releaseDate']
		date_object = datetime.datetime.strptime(releaseDate,'%b %d %Y')
		title=request.POST['title']
		movieLength=request.POST['movieLength']
		description=request.POST['description']
		language = request.POST['language']
		genre = request.POST['language']
		movieObj=Movie(imageName=imageName,releaseDate=date_object,title=title,movieLength=movieLength,description=description)
		movieObj.save()
		languageObj = Language(LANGUAGECHOICES=language)
		languageObj.save()
		genreObj = Genre(GENRECHOICES=genre)
		genreObj.save()
		categoryObj = Category(language=languageObj.LANGUAGECHOICES,genre=genreObj.GENRECHOICES)
		categoryObj.save()
		ralationshipObj = Relationship(taxonomyId=categoryObj,movieId=movieObj)
		relationshipObj.save()
		return HttpResponse(json.dumps({"validation": "Delails saved successfully","status":True}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"validation": "Something Went Wrong","status":False}), content_type="application/json")