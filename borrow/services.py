from borrow.models import *
from django.db import transaction
from rest_framework.exceptions import PermissionDenied, ValidationError
from datetime import timedelta, date, datetime

class BorrowServices:
    @staticmethod
    def create_borrow(user_id, cart_id):
        with transaction.atomic():
            cart = Cart.objects.get(pk=cart_id)
            cart_items = cart.items.all()
            # cart_items = cart.items.select_related('book').all()
    
            borrow = Borrow.objects.create(
                user_id=user_id
            )
    
            borrow_items = [
                BorrowItem(
                    borrow = borrow,
                    book = item.book,
                    return_date = date.today() + timedelta(days=30)
                )
                for item in cart_items
            ]
            BorrowItem.objects.bulk_create(borrow_items)
    
            cart.delete()
    
            return borrow

