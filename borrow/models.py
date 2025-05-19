from django.db import models
from users.models import User

# Create your models here.
# Member Model-->
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
