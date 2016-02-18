from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView 
from models import Movie,Category,Language,Genre,Relationship
import json, datetime
from django.shortcuts import render

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

def show_movies_filter_by_language(request):
	jsonObj = json.loads(request.body)
	languageId = jsonObj['languageId']
	ralationshipObj = Relationship.objects.filter(taxonomyId__language__id=languageId)
	movieList = []
	for i in relationshipObj:
		image = str(i.movie.image).split('.')[0]+'.png'
		date = int(i.movie.releaseDate.strftime('%s'))*1000
		movieObj = {"title":i.movie.title,"description":i.movie.description,"image":"Media/"+image,"releaseDate":i.movie.date}
		movieList.append(movieObj)
	return HttpResponse(json.dumps({"movieList":movieList,"status":True}), content_type="application/json")

def show_movies_filter_by_language(request):
	jsonObj = json.loads(request.body)
	genreId = jsonObj['genreId']
	ralationshipObj = Relationship.objects.filter(taxonomyId__language__id=genreId)
	movieList = []
	for i in relationshipObj:
		image = str(i.movie.image).split('.')[0]+'.png'
		date = int(i.movie.releaseDate.strftime('%s'))*1000
		movieObj = {"title":i.movie.title,"description":i.movie.description,"image":"Media/"+image,"releaseDate":i.movie.date}
		movieList.append(movieObj)
	return HttpResponse(json.dumps({"movieList":movieList,"status":True}), content_type="application/json")
