from django.urls import path

from . import views
from .views import *

from django.conf import settings   #questi import servono per servire i file static uploadati da un utente
from django.conf.urls.static import static

urlpatterns = [
    path('', globalView.as_view(), name='pittogrammi-list'),
    path('create_h', h_create.as_view(), name='h-create'),
    path('item/<int:pk>/h_update', h_update.as_view(), name='h-update'),
    path('delete_entry_h/<int:pk>', views.h_delete.as_view(), name='p_delete_h'),
    path('create_p', p_create.as_view(), name='p-create'),
    path('item/<int:pk>/p_update', p_update.as_view(), name='p-update'),
    path('delete_entry_p/<int:pk>', views.p_delete.as_view(), name='p_delete_p'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
