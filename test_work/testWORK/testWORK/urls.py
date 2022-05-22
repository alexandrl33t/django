
from django.contrib import admin
from django.urls import path, include
from vopros.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/', )
    path('quetion/create/', CreateQuetionApiView.as_view()), #создание вопроса
    path('quetion/update/<int:pk>', UpdateQuetionApiView.as_view()), #редактирование вопроса (только автор вопроса)
    path('quetion/delete/<int:pk>', DestroyQuetionApiView.as_view()), #удаление вопроса (только для автора автора)
    path('category/',TagApiView.as_view()), #вывести все категории
    path('quetion/all', ShowQuetionsApiView.as_view()), #вывести все вопросы
    path('quetion/<int:pk>/', CurrentQuetionApiView.as_view()), #получение ответов на конкрентый вопрос по pk
    path('quetion/<int:pk>/add-answer', AnswerApiView.as_view())
]
