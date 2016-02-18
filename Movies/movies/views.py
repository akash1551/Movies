from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView 
from models import Movie,Language,Genre
import json, datetime
from django.shortcuts import render
from django.db.models import Q

def landing_page(request):
	return render_to_response('landing_page.html')

def get_language_and_genre(request):
	languageObj = Language.objects.all()
	genreObj = Genre.objects.all()
	languageList = []
	genreList = []
	sortByList = [{"id":1,"name":"Length", "tag": "SORT"}, {"id":2,"name":"Release Date", "tag": "SORT"}]
	for i in languageObj:
		obj = {"id":i.id,"name":i.name, "tag": "LANGUAGE"}
		languageList.append(obj)
	for i in genreObj:
		obj = {"id":i.id,"name":i.name, "tag": "GENRE"}
		genreList.append(obj)
	return HttpResponse(json.dumps({"sortByList": sortByList, "languageList":languageList,"genreList":genreList,"status":True}), content_type="application/json")
	
def movies_by_filter(request):
	jsonObj = json.loads(request.body)
	selectedFilterList = jsonObj['selectedFilterList']
	pageNo = jsonObj['pageNo']
	totalEntries = jsonObj['totalEntries']
	exclude_page_entries = (pageNo - 1) * totalEntries
	next_page_entries = exclude_page_entries + totalEntries
	if len(selectedFilterList) == 0:
		movie_listing_objs_list = Movie.objects.all().distinct()[exclude_page_entries:next_page_entries]
		total_entries = Movie.objects.all().distinct()
		total_entries = len(total_entries)
		print 'total_entries------>', total_entries
	else:
		language_list = []
		genre_list = []
		
		for obj in selectedFilterList:
			if obj['tag'] == "LANGUAGE":
				language_list.append(obj['name'].strip())
			if obj['tag'] == "GENRE":
				genre_list.append(obj['name'].strip())
	
		query_list = []
		if len(language_list) != 0:
			print 'language_list-->', language_list
			language_query = reduce(lambda x, y: x | y, [Q(language__name__iexact=word) for word in language_list])
			query_list.append(language_query)
		if len(genre_list) != 0:
			print 'genre_list-->', genre_list
			genre_query = reduce(lambda x, y: x | y, [Q(genre__name__iexact=word) for word in genre_list])
			query_list.append(genre_query)

		if len(query_list) != 0:
			print 'query_list-->', query_list
			movie_listing_objs_list = Movie.objects.filter(reduce(lambda x, y: x & y, query_list)).distinct()[exclude_page_entries:next_page_entries]
			total_entries = movie_listing_objs_list.count()
			print total_entries
		else:
			movie_listing_objs_list = Movie.objects.all().distinct()[exclude_page_entries:next_page_entries]
			total_entries = movie_listing_objs_list.count()
			print total_entries
			print 'total_entries-->', total_entries

	movie_list = []
	for i in movie_listing_objs_list:
		date = int(i.releaseDate.strftime("%s")) * 1000
		language_list = []
		genre_list = []
		[language_list.append(j.name) for j in i.language.all()]
		[genre_list.append(j.name) for j in i.genre.all()]
		obj={"imageUrl": 'Media/'+str(i.image),"releaseDate": date,"title": i.title,"movieLength": i.movieLength,"description": i.description,"language_list":language_list,"genre_list":genre_list}
		movie_list.append(obj)
	if len(movie_list) != 0:
		return HttpResponse(json.dumps({'movieList':movie_list, 'status': True, 'pageNo': pageNo, 'totalEntries': total_entries}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'validation':"Record  not found..!!", 'status': False}), content_type="application/json")

