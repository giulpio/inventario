from django.urls import path

from . import views
from .views import *

# questi import servono per servire i file static uploadati da un utente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', list_all.as_view(), name='certificazioni-list'),
    path('create', create.as_view(), name='certificazioni-create'),
    path('item/<int:pk>/update', update.as_view(), name='certificazioni-update'),
    path('delete_entry/<int:pk>', views.delete.as_view(),
         name='certificazioni-delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
