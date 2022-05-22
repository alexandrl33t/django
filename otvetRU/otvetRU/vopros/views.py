import imp
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.test import tag
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from multiprocessing import context
from unicodedata import name
from django import http
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseNotFound

from .forms import *

from .models import *



class Quetions(ListView):
    paginate_by = 5 #нумирация страниц (максимум 5 элемнтов)
    model = Quetion
    template_name = 'vopros/index.html'
    context_object_name = 'quetions'
    extra_context = {'tittle':'Главная страница'}

class QutionsCategory(ListView):
    model = Quetion
    template_name= 'vopros/index.html'
    context_object_name = 'quetions'

    def get_queryset(self):
        return Quetion.objects.filter(slug = self.kwargs['cat_slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = Tag.objects.get(slug = self.kwargs['cat_slug'])
        context['tittle'] = str(tag.tag_name)
        context['quetions'] = Quetion.objects.filter(tag_name= tag.tag_name).values()
        return context   
         
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'vopros/register.html'
    success_url = reverse_lazy('home')
    extra_context = {'tittle':'Регистрация'}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):    
    form_class = LoginUserForm
    template_name = 'vopros/login.html'
    extra_context = {'tittle':'Авторизация'}

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('home')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def errorquetion(request):
    return HttpResponseNotFound('<h1>Задавать вопросы могут только авторизированные пользователи</h1>')

def addquetion(request):
    form = AddQuetion()  
    return render(request, 'vopros/addquetion.html', {'form':form})

def show_quetion(request, q_slug):
    quetion = get_object_or_404(Quetion, slug = q_slug)
    if quetion.time_create == quetion.time_update:
        time = quetion.time_create
    else:
        time = quetion.time_update    
    context = {
        'quetion': quetion,
        'tittle': quetion.tittle,
        'time':time,
        'tag_selected': quetion.tag_name,
        'q_slug':q_slug
    }
    return render(request, 'vopros/quetion.html', context=context)

#выборка по категории через функцию
# def show_cat_list(request, cat_slug):
#     tag = Tag.objects.get(slug= cat_slug)
#     quetions = Quetion.objects.filter(tag_name= tag.tag_name).values()
#     context = {
#         'tittle':tag.tag_name,
#         'quetions':quetions
#     }
#     return render(request, 'vopros/index.html', context=context)   
