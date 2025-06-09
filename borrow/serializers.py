from rest_framework import serializers
from borrow.models import *
from library.models import Book
from borrow.services import BorrowServices

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
    details = SimpleBookDetailsSerializers(source='book')
    class Meta:
        model = CartItem
        fields = ['id','book','details']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id','user','items']
        read_only_fields = ['user']

class CreateBorrowSerializers(serializers.Serializer):
    cart_id = serializers.UUIDField()

    def validate_cart_id(self, cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('No cart found with this id')
        if not CartItem.objects.filter(cart_id=cart_id).exists():
            raise serializers.ValidationError('Cart is empty')
        return cart_id
    
    def create(self, validated_data):
        user_id = self.context['user_id']
        cart_id = validated_data['cart_id']
        
        try:
            borrow = BorrowServices.create_borrow(user_id=user_id, cart_id=cart_id)
            return borrow
        except ValueError as error:
            raise serializers.ValidationError(str(error))
    
    def to_representation(self, instance):
        return BorrowSerializer(instance).data

class BorrowItemSerializer(serializers.ModelSerializer):
    book = SimpleBookDetailsSerializers(read_only=True)
    class Meta:
        model = BorrowItem
        fields = ['id','book','borrow_date','return_date']

class BorrowSerializer(serializers.ModelSerializer):
    items = BorrowItemSerializer(many=True, read_only=True)
    class Meta:
        model = Borrow
        fields = ['id','user','created_at','status','items']

class UpdateBorrowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = ['status']

class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

