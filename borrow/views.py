from django.shortcuts import render
from borrow.serializers import *
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin

class CartViewSet(CreateModelMixin, DestroyModelMixin,GenericViewSet,RetrieveModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartItemViewSet(ModelViewSet):
    # queryset = CartItem.objects.all()
    # serializer_class = CartItemSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(
            cart_id = self.kwargs['cart_pk']
        )
    
    def get_serializer_context(self):
        return {'cart_id' : self.kwargs['cart_pk']}