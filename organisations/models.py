from django.db import models
from datetime import datetime

# Create your models here.

class events(models.Model):
    EventName = models.CharField(max_length=100)
    EventDate = models.DateField()
    EventYear = models.IntegerField(default=0)

    def __str__(self):
        return self.EventName

class event_info(models.Model):
    events = models.ForeignKey(events,on_delete = models.CASCADE)
    venue = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    

class images(models.Model):
    events = models.ForeignKey(events,on_delete = models.CASCADE)
    # image = models.ImageField(null=True, blank=True, )
    # image = models.ImageField(null=True, blank=True, upload_to='static/event_images/%y',)
    image = models.ImageField(upload_to = "img/%y")
    date_time = models.DateTimeField(default=datetime.now(),blank=True)
    

    

   
    

