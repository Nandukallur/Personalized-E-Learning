from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('home/',HomeView.as_view(),name='h'),
    path('Registration/',RegView.as_view(),name="reg"),
    path('profile/',Profile.as_view(),name='pro'),
    path('proupdate/<int:pk>/',ProfileUpdateView.as_view(),name="proupd"),
    path('score_table/', ScoreTable.as_view(), name='ScoreTable'),
    path('send_certificate_email/', send_certificate_email, name='send_certificate_email'),
    path('ProgressCard/', ProgressCard.as_view(), name='ProgressCard'),
    path('resetpwd/', auth_views.PasswordResetView.as_view(template_name="./frpwd1.html"), name='resetpwd'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="./fgtpwdab.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="./newpwd1.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="./pwdresetdone.html"), name='password_reset_complete'),
    path('htmlcertificate/', htmlcertificate, name='htmlcertificate'),
    path('pythoncertificate/', pythoncertificate, name='pythoncertificate'),
    path('phpcertificate/', phpcertificate, name='phpcertificate'),
    path('generate-certificate/', generate_certificate, name='generate_certificate'),
    path('send-certificate-email/', send_certificate_email, name='send_certificate_email'),
    path('download-certificate/', download_certificate, name='download_certificate'),
    path('generate-pythoncertificate/', generate_pythoncertificate, name='generate_pythoncertificate'),
    path('send-pythoncertificate_email/', send_pythoncertificate_email, name='send_pythoncertificate_email'),
    path('download-pythoncertificate/', download_pythoncertificate, name='download_pythoncertificate'),
    path('generate-phpcertificate/', generate_phpcertificate, name='generate_phpcertificate'),
    path('send-phpcertificate-email/', send_phpcertificate_email, name='send_phpcertificate_email'),
    path('download-phpcertificate/', download_phpcertificate, name='download_phpcertificate'),
    path('feedies/',feedback, name='feedback'),
    path('submitfeedback/',submit_feedback.as_view(), name='feedbacks'),
    path('feed/',Feedbacks.as_view(),name="feed"),
    path('contactus/',Contact,name="contact"),
    path('project_list/', project_list, name='project_list'),

]
