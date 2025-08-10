from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name='notes-list'),
    path('<uuid:note_id>/', views.note_detail, name='note-detail'),
]
