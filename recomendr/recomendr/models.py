from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    name = models.CharField(max_length = 128)
    

class Course(models.Model):
    title = models.CharField(max_length = 512)
    department = models.CharField(max_length = 4)
    course_number = models.IntegerField()
    description = models.TextField()
    taken_by = models.ManyToManyField(User)
    
class Tag(models.Model):
    tag_name = models.CharField(max_length=512)
    courses = models.ManyToManyField(Course)
    
class CourseInstance(models.Model):
    
    FALL = 'FA'
    WINTER = 'WN'
    SPRING = 'SP'
    SUMMER = 'SU'
    QUARTER_CHOICES = (
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
    )
    
    
    year = models.IntegerField()
    quarter = models.CharField(max_length=2,
                               choices=QUARTER_CHOICES)
    
    professor = models.ForeignKey(Professor)
    course = models.ForeignKey(Course)
    
    