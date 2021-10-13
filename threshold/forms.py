from django import forms
from .models import SetThreshold

class SetThresholdForm(forms.ModelForm):
    class Meta:
        model = SetThreshold
        fields = ['threshold',]