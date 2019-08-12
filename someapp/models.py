from django.db import models
from django.contrib.auth.models import User

# Create your models here.



def get_location(instance,filename):
    return filename.split('.')[-1]+"/"+filename

class Comments(models.Model):
    username=models.CharField(max_length=5,default="Anonymous")
    content=models.TextField()
   # fil=models.FileField(upload_to=get_location,null=True)




    def __str__(self):
        return self.username

