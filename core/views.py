from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import NoteAIForm, TranslationForm, NoteForm
from .models import Note
from .utils import (
    generate_gemini_response,
    generate_summary,
    generate_analysis,
    translate_content,
    improve_grammar,
)

# Home Page
def home(request):
    return render(request, 'home.html')

# Register View
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created. You can now log in.')
            return redirect('login')

    return render(request, 'register.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'login.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('login')

# Notes List View
@login_required
def notes_list(request):
    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes_list.html', {'notes': notes})

# Create Note
@login_required
def note_create(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        note = form.save(commit=False)
        note.user = request.user
        note.save()
        return redirect('notes_list')
    return render(request, 'note_form.html', {'form': form})

# Edit Note
@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('notes_list')
    return render(request, 'note_form.html', {'form': form})

# About Page
def about(request):
    return render(request,'about.html')

# Delete Note
@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'note_confirm_delete.html', {'note': note})

# AI Tools View
@login_required
def note_ai_tools(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    response = None
    translated = None

    if request.method == "POST":
        if 'save_summary_analysis' in request.POST:
            form = NoteAIForm(request.POST, instance=note)
            if form.is_valid():
                form.save()
                messages.success(request, "AI-generated content saved successfully.")
                return redirect('note_ai_tools', pk=pk)

        elif 'translate' in request.POST:
            trans_form = TranslationForm(request.POST)
            if trans_form.is_valid():
                lang = trans_form.cleaned_data['language_code']
                result = translate_content(note.content, lang)
                if result.startswith("❌"):
                    messages.error(request, "Translation failed.")
                else:
                    translated = result

        elif 'tool' in request.POST:
            tool = request.POST.get("tool")
            if tool == "summarize":
                result = generate_summary(note.content)
                if result.startswith("❌"):
                    messages.error(request, "Summary generation failed.")
                else:
                    note.summary = result
                    note.save()
                    messages.success(request, "Summary generated and saved.")
            elif tool == "analyze":
                result = generate_analysis(note.content)
                if result.startswith("❌"):
                    messages.error(request, "Analysis generation failed.")
                else:
                    note.analysis = result
                    note.save()
                    messages.success(request, "Analysis generated and saved.")
            elif tool == "improve":
                result = improve_grammar(note.content)
                if result.startswith("❌"):
                    messages.error(request, "Grammar improvement failed.")
                else:
                    note.content = result
                    note.save()
                    messages.success(request, "Grammar improved and saved.")

    form = NoteAIForm(instance=note)
    trans_form = TranslationForm()

    return render(request, "note_ai_tools.html", {
        "note": note,
        "form": form,
        "trans_form": trans_form,
        "translated": translated
    })
