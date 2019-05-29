from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class NeighbourHood(models.Model):
    neighbourhood_name = models.CharField(max_length = 100)
    neighbourhood_location = models.CharField(max_length = 100)
    occupants_count = models.IntegerField()

    def __str__(self):
        return self.neighbourhood_name

class User(models.Model):
    full_name = models.CharField(max_length = 100)
    profile_pic = models.ImageField(upload_to = 'images/', blank = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    neighbourhood = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    userId =models.IntegerField(default = 0)
    user_email = models.EmailField()

    def __str__(self):
        return self.full_name

class Businesses(models.Model):
    business_name = models.CharField(max_length = 150)
    user = models.ForeignKey(User,on_delete = models.CASCADE,null = True)
    neighbourhood_id = models.ForeignKey(NeighbourHood,on_delete = models.CASCADE,null = True)
    business_email = models.EmailField()

class Posts(models.Model):
    title = models.CharField(max_length = 60)
    post = models.TextField(blank= True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    poster_id = models.IntegerField(default=0)

    class Meta:
        ordering = ['-id']