from django.db import models
from users.models import User
from uuid import uuid4
from library.models import *

# Create your models here.
# Member Model-->
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="cart"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.first_name}"

class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name="items"
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
    )
    class Meta:
        unique_together = [['cart','book']]
    
    def __str__(self):
        return f"{self.book.title}"