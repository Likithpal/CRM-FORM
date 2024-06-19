# crm/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete_guest/<int:guest_id>/', views.delete_guest, name='delete_guest'),
    path('revert_guest/<int:guest_id>/', views.revert_guest, name='revert_guest'),
    path('edit_guest/<int:id>/', views.edit_guest, name='edit_guest'),
]
