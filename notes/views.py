from django.shortcuts import render
from .models import Note

# Create your views here.

def show_all_notes(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', { 'notes': all_notes })