from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustUser(AbstractUser):
    
    phone=models.IntegerField(null=True)
    options=(
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    )
    gender=models.CharField(max_length=100,choices=options,null=True,default='Male')
    age=models.IntegerField(null=True)


class pdfnotes(models.Model):
    pdff = models.FileField(upload_to="notes")





class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
