from django.urls import path
from . import views
from .views import *

from django.conf import settings   #questi import servono per servire i file static uploadati da un utente
from django.conf.urls.static import static

urlpatterns = [
    path('', test_list.as_view(), name='test-list'),
    path('item/<int:pk>', test_detail.as_view(), name='test-detail'),
    path('item/<int:pk>/update', test_update.as_view(), name='test-update'),
    path('create_test', create_test.as_view(), name='test-create'),
    path('delete_entry/<int:pk>', views.test_delete.as_view(), name='delete_test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
