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
	sortByList = [{"id":1,"name":"Length", "tag": "SORT", "isSelected": False, "databaseSortParameter": "movieLength"}, {"id":2,"name":"Release Date", "tag": "SORT", "isSelected": False, "databaseSortParameter": "-releaseDate"}]
	for i in languageObj:
		obj = {"id":i.id,"name":i.name, "tag": "LANGUAGE", "isSelected": False}
		languageList.append(obj)
	for i in genreObj:
		obj = {"id":i.id,"name":i.name, "tag": "GENRE", "isSelected": False}
		genreList.append(obj)
	return HttpResponse(json.dumps({"sortByList": sortByList, "languageList":languageList,"genreList":genreList,"status":True}), content_type="application/json")
	
def movies_by_filter(request):
	jsonObj = json.loads(request.body)
	selectedFilterList = jsonObj['selectedFilterList']
	pageNo = jsonObj['pageNo']
	totalEntries = jsonObj['itemPerPage']
	excludePageEntries = (pageNo - 1) * totalEntries
	nextPageEntries = excludePageEntries + totalEntries
	if len(selectedFilterList) == 0:
		movieListingObjsList = Movie.objects.all().distinct()[excludePageEntries:nextPageEntries]
		totalEntries = Movie.objects.all().distinct()
		totalEntries = len(totalEntries)
		print 'totalEntries------>', totalEntries
	else:
		languageList = []
		genreList = []
		sortList = []
		
		for obj in selectedFilterList:
			if obj['tag'] == "LANGUAGE":
				languageList.append(obj['name'].strip())
			if obj['tag'] == "GENRE":
				genreList.append(obj['name'].strip())
			if obj['tag'] == "SORT":
				sortList.append(obj['databaseSortParameter'].strip())
	
		queryList = []
		if len(languageList) != 0:
			print 'languageList-->', languageList
			language_query = reduce(lambda x, y: x | y, [Q(language__name__iexact=word) for word in languageList])
			queryList.append(language_query)
		if len(genreList) != 0:
			print 'genreList-->', genreList
			genre_query = reduce(lambda x, y: x | y, [Q(genre__name__iexact=word) for word in genreList])
			queryList.append(genre_query)

		sortListParameter = []
		if len(sortList) != 0:
			print 'sortList-->', sortList
			genre_query = [sortListParameter.append(word) for word in sortList]

		if len(queryList) != 0:
			print 'queryList-->', queryList
			movieListingObjsList = Movie.objects.filter(reduce(lambda x, y: x & y, queryList)).order_by(*sortListParameter).distinct()[excludePageEntries:nextPageEntries]
			totalEntries = movieListingObjsList.count()
			print totalEntries
		else:
			movieListingObjsList = Movie.objects.all().order_by(*sortListParameter).distinct()[excludePageEntries:nextPageEntries]
			totalEntries = movieListingObjsList.count()
			print totalEntries
			print 'totalEntries-->', totalEntries

	movieList = []
	for i in movieListingObjsList:
		date = int(i.releaseDate.strftime("%s")) * 1000
		languageList = []
		genreList = []
		[languageList.append(j.name) for j in i.language.all()]
		[genreList.append(j.name) for j in i.genre.all()]
		obj={"imageUrl": 'Media/'+str(i.image),"releaseDate": date,"title": i.title,"movieLength": i.movieLength,"description": i.description,"languageList":languageList,"genreList":genreList}
		movieList.append(obj)
	if len(movieList) != 0:
		return HttpResponse(json.dumps({'movieList':movieList, 'status': True, 'pageNo': pageNo, 'totalEntries': totalEntries}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'validation':"Record  not found..!!", 'status': False}), content_type="application/json")

