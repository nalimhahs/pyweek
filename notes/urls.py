from django.urls import path
from .views import show_all_notes, show_single_note, add_note

urlpatterns = [
    path('', show_all_notes, name='show_all_notes'),
    path('<int:note_id>', show_single_note, name='show_single_note'),
    path('add', add_note, name='add_note'),
]
