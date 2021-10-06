from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadFile

def uploadfile(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        type = request.POST['type']
        uploadfile = UploadFile(
            title = title,
            description = description,
            file = file,
            type = type,
        )
        uploadfile.save()
        return redirect('uploader:uploader')
    else:
        uploadfileForm = UploadFileForm
        context = {
            'uploadfileForm': uploadfileForm,
        }
        return render(request, 'uploader/uploader.html', context)