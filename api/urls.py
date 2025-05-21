from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from library.views import *
from borrow.views import *

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
# router.register('members', MemberViewSet)
router.register('authors', AuthorViewSet)
router.register('carts', CartViewSet)

# member_router = routers.NestedDefaultRouter(router,'members',lookup='member')
# member_router.register('borrows', BorrowRecordViewSet, basename='borrow-books')

book_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_router.register('reviews',ReviewViewSet, basename='book-reviews')

cart_router = routers.NestedDefaultRouter(router,'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('',include(router.urls)),
    # path('',include(member_router.urls)),
    path('',include(book_router.urls)),
    path('',include(cart_router.urls)),
]