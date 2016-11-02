from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def stringmaker():
    return "<h3> HEY THIS IS A FUNCTION </h3>"
def index(request):
    context_dict = {'boldmessage' : "Crunchy, creamy cookies"}
    return render(request, 'rango/index.html', context=context_dict)
    

def about(request):
    return HttpResponse("Rango says hey hi this is all about the about page <br/> <a href = '/rango/'> Rango Home </a>" + stringmaker())