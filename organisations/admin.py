from django.contrib import admin
from . models import events
from . models import event_info
from . models import images

# Register your models here.

admin.site.register(events)
admin.site.register(event_info)
admin.site.register(images)