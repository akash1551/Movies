from django.contrib import admin
admin.autodiscover()
from models import Movie, Language, Genre
# Register your models here.
admin.site.register(Movie)
admin.site.register(Language)
admin.site.register(Genre)