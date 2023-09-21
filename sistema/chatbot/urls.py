from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [

    path('chatbot/', views.chat, name='chat'),
    path('get_response/', views.get_response, name='get_response'),

]