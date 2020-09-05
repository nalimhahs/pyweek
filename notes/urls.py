from django.urls import path
from .views import show_all_notes

urlpatterns = [
    path('', show_all_notes, name='show_all_notes'),
    # path('add', add_note, name='add_note'),
]
