from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from library.models import *
from library.serializers import *
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from library.filters import BookFilters
from library.paginations import DefaultPagination

# CategoryViewSet -->
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(book_count=Count('books')).all()
    serializer_class = CategorySerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    # queryset = Book.objects.all()
    queryset = Book.objects.select_related('author', 'category').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilters
    search_fields = ['title']
    ordering_fields = ['category']
    pagination_class = DefaultPagination

'''
class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowRecordViewSet(ModelViewSet):
    queryset = BorrowRecord.objects.all()
    serializer_class = BorrowRecordSerializer
'''

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(
            book_id = self.kwargs['book_pk']
        )

    def get_serializer_context(self):
        return {'book_id' : self.kwargs['book_pk']}
    """ Note:
    ViewSet er modde always ekta 'kwargs' thake, jekane 'domain_pk' name e product ta thake.
    Eai khatree 'domain' holo 'book'. So specific product/book er id ta pabo 'book_pk' name e.
    """