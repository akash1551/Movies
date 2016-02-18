from django.contrib import admin
admin.autodiscover()
from models import Movie,Category,Relationship
# Register your models here.
admin.site.register(admin)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Relationship)