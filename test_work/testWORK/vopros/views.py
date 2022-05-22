from urllib import request
from webbrowser import get
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from vopros.permissions import *
from vopros.serializers import *
from .models import *

class CreateQuetionApiView(generics.ListCreateAPIView): #создание вопросов 
    queryset = Quetion.objects.all()
    serializer_class = QuetionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        return Response("Напишите вопрос.")      

class ShowQuetionsApiView(generics.ListAPIView):
    queryset = Quetion.objects.all()
    serializer_class = QuetionSerializer

    

class UpdateQuetionApiView(generics.UpdateAPIView):
    queryset = Quetion.objects.all()
    serializer_class = QuetionSerializer
    permission_classes=(isAdminOrAuthor, IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
       quetion = Quetion.objects.get(pk = self.kwargs['pk']) 
       return Response({'quetion': QuetionSerializer(quetion).data})
    

class DestroyQuetionApiView(generics.DestroyAPIView):
    queryset = Quetion.objects.all()
    serializer_class = QuetionSerializer 
    permission_classes=(isAdminOrAuthor, IsAuthenticatedOrReadOnly, )       

    def get(self, request, *args, **kwargs):
       quetion = Quetion.objects.get(pk = self.kwargs['pk']) 
       return Response({'quetion': QuetionSerializer(quetion).data})

class CurrentQuetionApiView(APIView):
    def get(self, request, *args, **kwargs):
        answers = Answer.objects.filter(quetionId = self.kwargs['pk'])
        quetion = Quetion.objects.get(pk = self.kwargs['pk'])
        return Response({'quetion': QuetionSerializer(quetion).data,
                        'answers': AnswerSerializer(answers, many = True).data                        
        })
    def delete(self, request, *args, **kwargs):
        del_object = self.get_object(self.kwargs['pk'])
        del_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    # def post(self, request, *args, **kwargs):
    #     answers = Answer.objects.all()
    #     return Response({'answers': AnswerSerializer(answers).data})
        

class TagApiView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer 

class AnswerApiView(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
     


        
    