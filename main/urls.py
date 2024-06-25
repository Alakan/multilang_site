# main/urls.py

from django.urls import path
from .views import article_list
from .views import chatbot

urlpatternes = [
    path('', article_list, name='article_list')
    path('chatbot/', chatbot, name='chatbot'),
]