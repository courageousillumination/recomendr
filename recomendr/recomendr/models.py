from django.db import models

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
    description = models.TextField()
    
