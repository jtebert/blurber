from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request, 'blurber/index.html', {}
    )

def about(request):
    return render(
        request, 'blurber/about.html', {}
    )