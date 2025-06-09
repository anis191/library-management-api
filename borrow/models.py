from django.db import models
from users.models import User
from uuid import uuid4
from library.models import *

# Member Model-->
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.email

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

class Borrow(models.Model):
    BORROWED = 'Borrowed'
    RETURNED = 'Returned'
    OVERDUE = 'Overdue'
    STATUS_CHOICES = [
        (BORROWED, 'Borrowed'),
        (RETURNED, 'Returned'),
        (OVERDUE, 'Overdue'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="borrows"
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=BORROWED,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Borrow {self.id} by {self.user.first_name}"

class BorrowItem(models.Model):
    borrow = models.ForeignKey(
        Borrow,
        on_delete=models.CASCADE,
        related_name="items"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    borrow_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField()

    def __str__(self):
        return f"{self.book.title} - return {self.return_date}"