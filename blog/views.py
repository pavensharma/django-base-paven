from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def x(request):
    fulltext = request.GET['fulltext']

    return render(request,'output.html', {'y':fulltext})