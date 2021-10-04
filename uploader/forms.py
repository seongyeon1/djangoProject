from django.forms import ModelForm
from .models import UploadFile

class UploadFileForm(ModelForm):
    class Meta:
        model = UploadFile
        fields = ['type', 'title', 'description', 'file']