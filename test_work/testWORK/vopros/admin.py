from django.contrib import admin
from .models import *

class QuetionAdmin(admin.ModelAdmin):
    list_display = ('id', 'tittle', 'photo', 'time_create')
    list_display_links = ('id','tittle')
    search_fields = ('tittle', 'content')
    prepopulated_fields = {'slug':('tittle',)}

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'count')
    search_fields = ('tag_name',)
    prepopulated_fields = {'slug':('tag_name',)}

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('quetionId', 'content', 'rating', 'time_create')
    search_fields = ('quetionId','content')

admin.site.register(Quetion, QuetionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Answer, AnswerAdmin)