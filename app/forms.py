from django import forms
from .models import FichierNotes

class UploadForm(forms.ModelForm):
    class Meta:
        model = FichierNotes
        fields = ['fichier']
