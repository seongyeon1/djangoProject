from django.forms import ModelForm
from .models import SetThreshold

class SetThresholdForm(ModelForm):
    class Meta:
        model = SetThreshold
        fields = ['threshold',]