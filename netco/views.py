# from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.

# def home(request):
#     return render(request,'index.html')

from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
from pytesseract import image_to_string



def home(request):
    return render(request, 'index.html')


# def analyze(request):
#     return render(request, 'analyze.html')


def index(request):
    if request.method == 'POST':
        Upload_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(Upload_file.name,Upload_file)
        x = image_to_string(Image.open('media/f7d83730_56_10_xDpvlS3.jpg'))
        return render(request,'index.html',{'text':x})
    else:
        return render(request,'index.html',{})
