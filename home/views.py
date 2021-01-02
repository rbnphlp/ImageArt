from django.shortcuts import render

# Create your views here.


def index(request):

    "A view to return undex page"
    "Add messages when delvery basket has only $2 "

    
    return render(request,'home/index.html')