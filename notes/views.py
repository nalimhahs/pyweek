from django.shortcuts import render
from .models import Note

# Create your views here.

def show_all_notes(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', { 'notes': all_notes })

def show_single_note(request, note_id):
    single_note = Note.objects.get(pk=note_id)
    return render(request, 'notes/single_note.html', { 'note': single_note })