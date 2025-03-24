from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile.pic")

    def __str__(self):
        return f"{self.user.username} Profile"
    

class post_data(models.Model):
    image_field =  models.ImageField(upload_to='images/')
    discriptions = models.TextField(null= True, blank= True)
