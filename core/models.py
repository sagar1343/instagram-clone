from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars")
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.user.username}:profile"


class Post(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="attachments")
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.caption[:10]} "
