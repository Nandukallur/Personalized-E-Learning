from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('basichtml/',basichtml_section,name='basichtml'),
    path('intermediatehtml/',intermediatehtml_section,name='interhtml'),
    path('advancedhtml/',advancedhtml_section,name='advhtml'),
    path('html_learn/',Basiclearn.as_view(),name='bhtml_learn'),
    path('intermediatehtml_learning/',intermediate_text_material,name='ihtml_learn'),
    path('advancedhtml_learning/',advanced_text_material,name='ahtml_learn'),
    path('htmlintro/', htmlintro, name='htmlintro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)