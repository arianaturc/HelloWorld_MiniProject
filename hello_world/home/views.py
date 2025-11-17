from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.
def index(request):
    message = Message.objects.first()  
    if message:
        return render(request, 'index.html', {'message' : message})
    else:
        return HttpResponse("No messages found in the database.")
