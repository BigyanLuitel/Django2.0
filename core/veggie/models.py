from django.db import models

# Create your models here.
class recipie(models.Model):
    recepie_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    recepie_image=models.ImageField(upload_to="recepies/",null=True, blank=True)
    