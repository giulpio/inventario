from django.urls import path

from . import views
from .views import *

# questi import servono per servire i file static uploadati da un utente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', globalView.as_view(), name='MS-list'),
    path('create_m', m_create.as_view(), name='manifacturer-create'),
    path('item/<int:pk>/update_m', m_update.as_view(), name='manifacturer-update'),
    path('delete_entry_m/<int:pk>', views.m_delete.as_view(),
         name='manifacturer-delete'),
    path('create_s', s_create.as_view(), name='selelr-create'),
    path('item/<int:pk>/update_s', s_update.as_view(), name='seller-update'),
    path('delete_entry_s/<int:pk>',
         views.s_delete.as_view(), name='seller-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
