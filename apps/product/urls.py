from django.conf.urls.static import static
from django.urls import path, include

from core.settings import base
from .views import *

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('category/', CategoryListView.as_view(), name='category'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/update/<int:pk>', update_cart_item, name='update_cart'),
    path('cart/add/<int:pk>', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:pk>', remove_from_cart, name='remove_from_cart'),
    path('type/', TypeListView.as_view(), name='type'),
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)