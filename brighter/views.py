from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = request.META.get('REMOTE_ADDR')
    context = {'custmessage': message}
    return render(request, "home.html", context)
