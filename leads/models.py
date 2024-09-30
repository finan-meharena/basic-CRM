from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): # inheriting fields lile first_name, last_name, email, is_staff..
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.user.username
    
class Lead(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, null=True, default=1)
    
    def __str__(self):
        return self.first_name
    

def post_user_created_signal(sender, instance, created, **kwargs):
   if created:
       UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
    
    