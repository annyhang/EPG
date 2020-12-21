from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

from .models import Recording
from .forms import RecordingForm
# Create your views here.

def upload_file_view(request):
    if request.method == 'POST':
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('annotate-view')
    else:
        form = RecordingForm()
    
    context = {
        'form': form,
    }
    return render(request, 'home.html', context)

def annotate_view(request):
    recordings = Recording.objects.all()
    context = {
        'recordings': recordings
    }
    return render(request, 'annotate.html', context)

def tutorial_view(request):
    return render(request, 'tutorial.html', {})

def delete_file(request, pk):
    if request.method == 'POST':
        recording = Recording.objects.get(pk=pk)
        recording.delete()
        return redirect('upload-file-view')