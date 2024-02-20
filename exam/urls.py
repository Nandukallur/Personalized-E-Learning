from django.urls import path
from .views import *
from accounts.views import upload_project, project_list,download_project
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('pyintro/',pythonintro.as_view(),name='pythonintro'),
    path('basic/',basic_section,name='basic'),
    path('b_learn/',learning_page.as_view(),name="b_learn"),
    path('intermediate/',intermediate_section,name='inter'),
    path('advanced/',advanced_section,name='adv'),
    path('basic_learning/',basic_video_material,name='b_video'),
    path('intermediate_learning/',intermediate_text_material,name='i_learn'),
    path('advanced_learning/',advanced_text_material,name='a_learn'),
    path('pythonintro/',pythonintro,name='pythonintro'),
    path('upload/', upload_project, name='upload_project'),
    path('project_list/', project_list, name='project_list'),
    path('download/<int:project_id>/', download_project, name='download_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
