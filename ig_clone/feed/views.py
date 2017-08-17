from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from feed.models import FileIt
from feed.forms import FileItForm

# Create your views here.
def upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILE['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'feed/upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    
    return render(request, 'feed/upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = FileItForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileItForm()
    
    return render(request, 'feed/model_form_upload.html', {
        'form': form
    })
