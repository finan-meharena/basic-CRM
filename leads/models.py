from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): # inheriting fields lile first_name, last_name, email, is_staff..
    pass

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class Lead(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE, null=True, default=1)
    
    def __str__(self):
        return self.first_name
    
    
    # SOURCE_CHOICES = (
    #     ('YouTube', "YouTube"),
    #     ("Google", "Google"),
    #     ("NewsLetter", "NewsLetter"),
    # )
    # phoned  = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)
    # profile_picture = models.ImageField(blank=True, null=True)  # needs pillow package to use ImageField
    # special_files = models.FileField(blank=True, null=True)
    
    