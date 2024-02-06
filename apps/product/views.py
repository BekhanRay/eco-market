from django.contrib.auth.decorators import login_required
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from apps.product.models import *
from apps.product.serializers import *


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class ProductDetailView(ListAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class CategoryListView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


class TypeListView(ListAPIView):

    queryset = Type.objects.all()
    serializer_class = TypeSerializer

    def list(self, request):
        qs = self.get_queryset()
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)


@login_required
class CartView(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.filter(user=None)
    serializer_class = CartSerializer

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)
        return cart

    def perform_update(self, serializer):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@login_required
def add_to_cart(request, product_id):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity += 1
    cart_item.save()

    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["PUT"])
@login_required
def update_cart_item(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    serializer = CartItemSerializer(cart_item, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, pk=cart_item_id)
    cart_item.quantity -= 1

    cart_item.save()
    return Response(str(cart_item.quantity), status=status)