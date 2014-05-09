from django.shortcuts import render, get_object_or_404

from recomendr.recomendr.models import *

import recomendr.recomendr.lda

def index(request):
    return render(request, "recomendr/index.html", {})
    
def all_courses(request):
    courses = Course.objects.all()
    return render(request, "recomendr/classes.html", {"classes": courses})

def course_page(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    similar_courses = recomendr.recomendr.lda.get_similar_courses(course, 10)
    print similar_courses
    return render(request, "recomendr/course.html", {"course": course, "similar_courses": similar_courses})