from django.urls import path

# import views

from . import views

urlpatterns = [
    path('index/', views.index, name="indexpage"),
    path('index/runcode/', views.runcode, name="runcode"),
]
