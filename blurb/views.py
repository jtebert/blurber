from django.shortcuts import render

# Create your views here.

def index(request):
    #profile = profile_from_request(request)

    return render(
        request, 'blurb/index.html', {}
    )