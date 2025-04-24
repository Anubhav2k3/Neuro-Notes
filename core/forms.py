from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']

class NoteAIForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['summary', 'analysis']

        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4, 'placeholder': 'AI-generated summary...'}),
            'analysis': forms.Textarea(attrs={'rows': 6, 'placeholder': 'AI-generated analysis...'}),
        }

class TranslationForm(forms.Form):
    language_code = forms.ChoiceField(
        choices=[
            ('en', 'English'), ('fr', 'French'), ('hi', 'Hindi'), ('es', 'Spanish'),
            ('de', 'German'), ('zh', 'Chinese'), ('ar', 'Arabic'), ('ru', 'Russian'),
            ('ja', 'Japanese'), ('pt', 'Portuguese')
        ],
        label='Translate to',
    )
