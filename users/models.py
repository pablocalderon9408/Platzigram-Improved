"""User models"""
# Django
from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    # is_staff = models.BooleanField(default=False)

    picture = models.ImageField(
        upload_to='users/pictures',
        default='img/instragram.png'
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
