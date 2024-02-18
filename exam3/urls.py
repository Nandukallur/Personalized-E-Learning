from django.urls import path
from .views import *

urlpatterns = [
    path('basicphp/',basicphp_section,name='basicphp'),
    path('intermediatephp/',intermediatephp_section,name='interphp'),
    path('advancedphp/',advancedphp_section,name='advphp'),
    # path('html_learn/',Basiclearn.as_view(),name='bhtml_learn')
    path('php_learn/',phplearning_page.as_view(),name='php_learn'),
    path('phpinter_learn/',phpinter_learn.as_view(),name='phpinter_learn'),
    path('phpadv_learn/',phplearnadv.as_view(),name='phpadv_learn'),
    path('phpintro/',phpintro,name='phpintro'),
]