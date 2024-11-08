from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')
from .models import Cat

def about(request):
    return render(request, 'about.html')

#Cats index
def cat_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})
