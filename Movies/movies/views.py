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
	if request.POST
		imageName=request.FILES['imageName']
		releaseDate=request.POST['releaseDate']
		date_object = datetime.datetime.strptime(iDate,'%m/%d/%Y')
		title=request.POST['title']
		movieLength=request.POST['movieLength']
		description=request.POST['description'] 
		movie=Movie(imageName=imageName,releaseDate=date_object,title=title,movieLength=movieLength,description=description)
		movie.save()
		return render_to_response('.html')
	else:
		return render_to_response('.html')

