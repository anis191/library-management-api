from django.contrib import admin
from borrow.models import Cart, CartItem, Borrow, BorrowItem, Member

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id','user']

# Register your models here.
# admin.site.register(Cart)
admin.site.register(Member)
admin.site.register(CartItem)
admin.site.register(Borrow)
admin.site.register(BorrowItem)
