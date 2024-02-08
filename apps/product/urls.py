from django.conf.urls.static import static
from django.urls import path, include

from core.settings import base
from . import views
from .views import *

urlpatterns = [
    path('product/', ProductListView.as_view(), name='product-list'),
    path('product/<int:id>/', ProductDetailView.as_view()),
    path('category/', CategoryListView.as_view(), name='category'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/update/<int:cart_item_id>', views.update_cart_item, name='update_cart'),
    path('cart/add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>', views.remove_from_cart, name='remove_from_cart'),
    path('type/', TypeListView.as_view(), name='type'),
    ] + static(base.MEDIA_URL, document_root=base.MEDIA_ROOT)
