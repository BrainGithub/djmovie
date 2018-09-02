from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from .models import Movie,MovieComent
# Register your models here.

class MovieComentAdmin(MarkdownModelAdmin):
    list_display = ('user','movie','date')

admin.site.register(Movie)
admin.site.register(MovieComent,MovieComentAdmin)
