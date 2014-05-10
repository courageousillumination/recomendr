from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required

from recomendr.recomendr.models import *
import recomendr.recomendr.lsi


def index(request):
    courses = Course.objects.all()
    return render(request, "recomendr/index.html", {"courses" : courses})
    
def all_courses(request):
    courses = Course.objects.all()
    return render(request, "recomendr/classes.html", {"classes": courses})

def course_page(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    similar_courses = recomendr.recomendr.lsi.get_similar_courses(course, 10)
    print similar_courses
    return render(request, "recomendr/course.html", {"course": course, "similar_courses": similar_courses})

def search(request):
    if request.method == "GET":
        name = request.GET["course_name"]
        courses = Course.objects.filter(title__icontains = name)
        if len(courses) == 1:
            return redirect('recomendr.course_page', course_id=courses[0].id)
        return render(request, "recomendr/classes.html", {"classes": courses})
        
    return redirect('index')

@login_required
def my_courses(request):
    if request.method == "POST":
        name = request.POST["course_name"]
        try:
            course = Course.objects.get(title = name)
        except:
            course = None
        if course:
            request.user.course_set.add(course)
            
    courses = Course.objects.all()
    my_courses = request.user.course_set.all()
    similar_courses = recomendr.recomendr.lsi.get_similar_courses_list(my_courses, 5)    
    
    return render(request, "recomendr/my_courses.html", {"courses" : courses, "my_courses" : my_courses, "suggested_courses" : similar_courses})