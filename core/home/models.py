from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
class car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name