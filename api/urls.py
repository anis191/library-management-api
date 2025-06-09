from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from library.views import *
from borrow.views import *
from users.views import SimpleUserViewSet

router = routers.DefaultRouter()
router.register('all_users', SimpleUserViewSet, basename='all_user')
router.register('members', MemberViewSet, basename='member')
router.register('categories', CategoryViewSet)
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('carts', CartViewSet)
router.register('borrows', BorrowViewSet, basename='borrow')

book_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
book_router.register('reviews',ReviewViewSet, basename='book-reviews')

cart_router = routers.NestedDefaultRouter(router,'carts', lookup='cart')
cart_router.register('items', CartItemViewSet, basename='cart-item')

urlpatterns = [
    path('',include(router.urls)),
    path('',include(book_router.urls)),
    path('',include(cart_router.urls)),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]