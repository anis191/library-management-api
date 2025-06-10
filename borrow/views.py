from django.shortcuts import render
from borrow.serializers import *
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from borrow.permissions import IsLibrarianOrAdminOrReadOnly, IsLibrarianOrAdmin
from rest_framework import permissions

class CartViewSet(CreateModelMixin, DestroyModelMixin,GenericViewSet,RetrieveModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        return serializer.save(user = self.request.user)

class CartItemViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(
            cart_id = self.kwargs.get('cart_pk')
        )
    
    def get_serializer_context(self):
        return {'cart_id' : self.kwargs.get('cart_pk')}

class BorrowViewSet(ModelViewSet):
    http_method_names = ['get','post','delete','put','head','options']
    
    @action(detail=True, methods=['put'])
    def update_status(self, request, pk=None):
        borrow = self.get_object()
        serializer = UpdateBorrowSerializers(
            borrow, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status' : 'Borrow status updated'})

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateBorrowSerializers
        elif self.action in ['update_status','put']:
            return UpdateBorrowSerializers
        return BorrowSerializer

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view',False):
            return Borrow.objects.none()
        
        if self.request.user.is_staff is True or self.request.user.role == User.LIBRARIAN:
            return Borrow.objects.prefetch_related('items__book__author','items__book__category').all()
            # return Borrow.objects.prefetch_related('items__book').all()
        return Borrow.objects.prefetch_related('items__book').filter(
            user = self.request.user
        )
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy', 'update_status']:
            return [IsLibrarianOrAdmin()]
        return [IsAuthenticated()]
    
    def get_serializer_context(self):
        return {'user_id' : self.request.user.id, 'user':self.request.user}

class MemberViewSet(ModelViewSet):
    serializer_class = MemberSerializers
    permission_classes = [IsLibrarianOrAdminOrReadOnly]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view',False):
            return Member.objects.none()
        
        if self.request.user.role == User.LIBRARIAN or self.request.user.is_staff:
            return Member.objects.all()
        return Member.objects.filter(
            user = self.request.user
        )
