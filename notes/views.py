from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm, MarkAsCompletedForm

# Create your views here.

def show_all_notes(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/all_notes.html', { 'notes': all_notes })

def show_single_note(request, note_id):
    single_note = Note.objects.get(pk=note_id)
    form = MarkAsCompletedForm(request.POST or None)
    if form.is_valid():
        if form.data['completed'] == 'on':
            single_note.completed = True
            single_note.save()
    return render(request, 'notes/single_note.html', { 'note': single_note, 'form': form })

def add_note(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.save()
        return redirect('show_single_note', note_id=note.pk)
    return render(request, 'notes/add_note.html', { 'form': form })