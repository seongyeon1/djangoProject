from django.shortcuts import render, redirect
from .forms import SetThresholdForm
from .models import SetThreshold

def setThreshold(request):
    if request.method == 'POST':
        threshold = request.POST['threshold']
        set_date = request.POST['set_date']

        setThreshold = SetThreshold(
            threshold = threshold,
            set_date = set_date,
        )
        setThreshold.save()
        return redirect('threshold:threshold')
    else:
        setThresholdForm = SetThresholdForm
        context = {
            'setThresholdForm': setThresholdForm,
        }
        return render(request, 'threshold/threshold.html', context)