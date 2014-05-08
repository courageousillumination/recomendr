from django.db import models

class Professor(models.Model):
    name = models.CharField(max_length = 128)
    

class Class(models.Model):
    
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
    title = models.CharField(max_length = 512)
    department = models.CharField(max_length = 4)
    course_number = models.IntegerField()
    description = models.TextField()
    professor = models.ForeignKey(Professor)
   
    
    
