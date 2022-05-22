import imp
from django.urls import path, include
from otvetRU import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', Quetions.as_view(), name='home'),
    path('quetion/<slug:q_slug>/', show_quetion, name = 'quetion'),
    path('create-quetion', addquetion, name='addquetion'),
    path('error', errorquetion, name='errorquetion'),
    path('category/<slug:cat_slug>', QutionsCategory.as_view(), name='category'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)