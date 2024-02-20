from django.urls import path
from .views import *
from accounts.views import upload_project3, project_list,download_project
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('phpint/',phpintro.as_view(),name='phpintro'),
    path('basicphp/',basicphp_section,name='basicphp'),
    path('intermediatephp/',intermediatephp_section,name='interphp'),
    path('advancedphp/',advancedphp_section,name='advphp'),
    # path('html_learn/',Basiclearn.as_view(),name='bhtml_learn')
    path('php_learn/',phplearning_page.as_view(),name='php_learn'),
    path('phpinter_learn/',phpinter_learn.as_view(),name='phpinter_learn'),
    path('phpadv_learn/',phplearnadv.as_view(),name='phpadv_learn'),
    path('phpintro/',phpintro,name='phpintro'),
    path('upload3/', upload_project3, name='upload_project3'),
    path('project_list/', project_list, name='project_list'),
    path('download/<int:project_id>/', download_project, name='download_project'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
