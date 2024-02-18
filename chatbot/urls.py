from django.urls import path
from .views import *

urlpatterns =[
    path('chatbot/', chatbot_view, name='chatbot'),
    path('bot/',ChatBotView.as_view(),name='bot')
]