from django.contrib import admin
from .models import CustUser,pdfnotes,Feedback,UploadedFile
# Register your models here.

admin.site.register(CustUser)
admin.site.register(pdfnotes)
admin.site.register(Feedback)
admin.site.register(UploadedFile)