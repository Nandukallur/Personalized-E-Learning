from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

class CustUser(AbstractUser):
    phone = models.IntegerField(null=True)
    options = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gender = models.CharField(max_length=100, choices=options, null=True, default='Male')
    age = models.IntegerField(null=True)
    is_active_basic = models.BooleanField(default=False,null=True,blank=True)
    is_active_inter = models.BooleanField(default=False,null=True,blank=True)
    is_active_adv = models.BooleanField(default=False,null=True,blank=True)
    is_active_coding = models.BooleanField(default=False,null=True,blank=True)

class pdfnotes(models.Model):
    pdff = models.FileField(upload_to="notes")


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_language = models.CharField(max_length=50)
    git_link = models.URLField()
    project_description = models.TextField()

    def __str__(self):
        return self.project_name



class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
