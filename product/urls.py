from django.urls import path

from . import views
from .views import *

# questi import servono per servire i file static uploadati da un utente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', views.home, name='home'),
    path('item/<int:pk>', product_detail.as_view(), name='product-detail'),
    path('item/<int:pk>/update', product_update.as_view(), name='product-update'),
    #path('create_new', product_create.as_view(), name='product-create'),
    path('', product_list.as_view(), name='product-list'),
    path('create_product', views.createProduct, name='create-product'),
    path('delete_entry/<int:pk>',
         views.product_delete.as_view(), name='delete_product'),
    path('ajax/change_status/', views.ajax_change_status,
         name='ajax_change_status')
    # path('item/<int:pk>/delete', product_delete.as_view(), name='delete-product1'),#creare template
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
