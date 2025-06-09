from rest_framework import serializers
from library.models import *

# CategorySerializer -->
class CategorySerializer(serializers.ModelSerializer):
    book_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ["id","name","description","book_count"]

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source = 'author.name')
    class Meta:
        model = Book
        fields = ['id','title','author','author_name','ISBN','category','availability_status']
        extra_kwargs = {
            'availability_status' : {'write_only' : True}
        }
    
    def validate_availability_status(self, value):
        if value is False:
            raise serializers.ValidationError("This book is not available!")
        return value
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','name','description','date']
    
    def create(self, validated_data):
        book_id = self.context['book_id']
        review = Review.objects.create(book_id=book_id, **validated_data)
        return review
    