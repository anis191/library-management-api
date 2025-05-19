from django_filters.rest_framework import FilterSet
from library.models import Book

class BookFilters(FilterSet):
    class Meta:
        model = Book
        fields = {
            'category_id' : ['exact'],
            'author__name' : ['icontains']
        }