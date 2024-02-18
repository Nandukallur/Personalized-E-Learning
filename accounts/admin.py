from django.contrib import admin
from .models import CustUser,pdfnotes,Feedback
# Register your models here.

admin.site.register(CustUser)
admin.site.register(pdfnotes)
admin.site.register(Feedback)
