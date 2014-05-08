from django.shortcuts import render

from recomendr.recomendr.models import *

def index(request):
    return render(request, "recomendr/index.html", {})
    
def all_classes(request):
    courses = Course.objects.all()
    return render(request, "recomendr/classes.html", {"classes": courses})
