from django.shortcuts import render
from .models import Permit

# Create your views here.
def index(request):
    permit =  Permit.objects.all()
    
    return render(request, 'permit_tracker/index.html', {'permit':  permit})