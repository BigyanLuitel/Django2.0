from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    recepie_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    recepie_image=models.ImageField(upload_to="recepies/",null=True, blank=True)
    recepie_view_count=models.IntegerField(default=1)
    
    