from django.shortcuts import render
from .models import PropertyCategory,Property

# Create your views here.
def contact(request):
    return render(request,'contact.html',{})

def properties(request):
    properties = Property.objects.all()

    return render(request,'properties.html', {'properties' : properties})

def home(request):
    pass

