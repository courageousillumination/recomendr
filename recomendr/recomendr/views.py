import random

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
    if request.method == "POST":
        tag_name = request.POST["tag_name"]
        #Normalize the name
        tag_name = tag_name.lower()
        tag_name = ' '.join([x.capitalize() for x in tag_name.split()])
        t, _ = Tag.objects.get_or_create(tag_name = tag_name)
        t.courses.add(course)
        
    tags = Tag.objects.all()
    similar_courses = recomendr.recomendr.lsi.get_similar_courses(course, 5)
    tagged_courses = [(tag, [x for x in tag.courses.all() if x != course]) for tag in course.tag_set.all()]
    my_tags = [(x, random.choice(y)) for x, y in tagged_courses if len(y) > 0]
    return render(request, "recomendr/course.html", {"course": course, "similar_courses": similar_courses, "tags" : tags, "my_tags" : my_tags})

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