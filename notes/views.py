from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import Note
from .ai_service import ai_service
import json


def index(request):
    """Display all notes"""
    notes = Note.objects.all()
    return render(request, 'notes/index.html', {'notes': notes})


def create_note(request):
    """Create a new note"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            note = Note.objects.create(title=title, content=content)
            messages.success(request, 'Note created successfully!')
            return redirect('edit_note', note_id=note.id)
        else:
            messages.error(request, 'Title and content are required.')
    
    return render(request, 'notes/create.html')


def edit_note(request, note_id):
    """Edit an existing note"""
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        note.title = request.POST.get('title', note.title)
        note.content = request.POST.get('content', note.content)
        note.save()
        messages.success(request, 'Note updated successfully!')
        return redirect('edit_note', note_id=note.id)
    
    return render(request, 'notes/edit.html', {'note': note})


def delete_note(request, note_id):
    """Delete a note"""
    if request.method == 'POST':
        note = get_object_or_404(Note, id=note_id)
        note.delete()
        messages.success(request, 'Note deleted successfully!')
    
    return redirect('index')


@csrf_exempt
@require_http_methods(["POST"])
def ai_action(request):
    """Handle AI-powered actions on notes"""
    try:
        data = json.loads(request.body)
        action = data.get('action')
        content = data.get('content')
        
        if not action or not content:
            return JsonResponse({'error': 'Action and content are required'}, status=400)
        
        result = ""
        
        if action == 'summarize':
            result = ai_service.summarize_note(content)
        elif action == 'improve_grammar':
            result = ai_service.improve_grammar(content)
        elif action == 'translate':
            result = ai_service.translate_to_hindi(content)
        elif action == 'analyze':
            result = ai_service.analyze_content(content)
        else:
            return JsonResponse({'error': 'Invalid action'}, status=400)
        
        return JsonResponse({'result': result})
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
