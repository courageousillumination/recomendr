from django.shortcuts import render

from recomendr.recomendr.models import *

def index(request):
    return render(request, "recomendr/index.html", {})
    
def all_classes(request):
    classes = Class.objects.all()
    return render(request, "recomendr/classes.html", {"classes": classes})
