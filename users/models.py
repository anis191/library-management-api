from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import CustomUserManager
# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'
    ROLE_CHOICES = [
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,null=True,blank=True,default=None)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
