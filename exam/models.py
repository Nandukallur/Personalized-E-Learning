from django.db import models

from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustUser

class TestResult(models.Model):
    user = models.ForeignKey(CustUser, on_delete=models.CASCADE)
    options=(
        ('Basic','Basic'),
        ('BasicHTML','BasicHTML'),
        ('BasicPHP','BasicPHP'),
        ('Intermediate','Intermediate'),
        ('IntermediateHTML','IntermediateHTML'),
        ('IntermediatePHP','IntermediatePHP'),
        ('Advanced','Advanced'),
        ('AdvancedHTML','AdvancedHTML'),
        ('AdvancedPHP','AdvancedPHP')
    )
    section=models.CharField(max_length=100,choices=options,default='Basic')
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)
    is_active_fields = models.BooleanField(default = False,null=True,blank = True)
    
 
