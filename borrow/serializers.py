from rest_framework import serializers
from borrow.models import *
from library.models import Book

class SimpleBookDetailsSerializers(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.name')
    category_name = serializers.ReadOnlyField(source = 'category.name')
    class Meta:
        model = Book
        fields = ['title','author_name','category_name','ISBN']

class AddCartItemSerializer(serializers.ModelSerializer):
    book_id = serializers.IntegerField()
    class Meta:
        model = CartItem
        fields = ['id','book_id']
    
    def save(self,**kwargs):
        cart_id = self.context['cart_id']
        book_id = self.validated_data['book_id']

        try:
            cart_check = CartItem.objects.get(
                cart_id=cart_id, book_id=book_id
            )
            raise serializers.ValidationError(
                f"You already added this book!"
            )
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(
                cart_id=cart_id, **self.validated_data
            )
            return self.instance
        
    def validate_book_id(self, value):
        available = Book.objects.filter(pk=value).exists()
        if available is not True:
            raise serializers.ValidationError(
                f"Book with id-{value} does not exists"
            )
        return value

class CartItemSerializer(serializers.ModelSerializer):
    # details = BookSerializer(source='book',read_only=True)
    details = SimpleBookDetailsSerializers(source='book')
    class Meta:
        model = CartItem
        fields = ['id','book','details']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id','user','items']
