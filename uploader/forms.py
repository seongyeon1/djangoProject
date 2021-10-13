from django.forms import ModelForm
from .models import UploadFile

from django import forms

class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = ['title', 'description', 'file']

# class UploadForm(forms.Form):
#     file = forms.FileField(widget=forms.FileInput(attrs={
#         'id': 'file_id'
#     }))
