from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    message = "Hello, world!"
    context = {'custmessage': message}
    return render(request, "home.html", context)
