from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.

def stringmaker():
    return "<h3> HEY THIS IS A FUNCTION </h3>"
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]  
    context_dict = {'categories': category_list}  

    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango says hey hi this is all about the about page " +
    "<br/> <a href = '/rango/'> Rango Home </a>" + stringmaker())
