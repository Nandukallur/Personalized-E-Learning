from django.urls import path
from .views import chatbot_view, ChatBotView

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot'),
    path('bot/', ChatBotView.as_view(), name='bot')
]
