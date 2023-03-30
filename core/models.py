from ssl import create_default_context
from django.db import models
from django.contrib.auth import get_user_model
import uuid#this helps us get a unique id for each of the posts
from datetime import datetime

#model of the currently logged in user
User = get_user_model()

# Create your models here.

class Profile(models.Model):
    #Using a foreign key, we'll link to the currently logged in user model
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to = 'profile_images', default = 'blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    #making this the primary key of each post replacing the one django gives automatically starting from 0 which is usually a long character
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user#we use self.user wkthout username bcos we are not passing in an obj and it is not a foreign key


class LikePost(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username 

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user