

# Create your views here.
from django.shortcuts import render,redirect
from django.conf import settings
from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from . import models
from . models import images
from . form import ImageForm

# from django.views.decorators.csrf import csrf_exempt
# import stripe

# stripe.api_key = settings.STRIPE_PRIVATE_KEY


#...........
def home(request):
    d={
        'title':'home',
    }
    return render(request,'home.html',d)


def about(request):
    d={
        'title':'about',
    }
    return render(request,'about.html',d)
def founders(request):
    return render(request,'founders.html')

def theme(request):
    return render(request,'theme.html')

def Health_Awareness(request):
    d = {
        'title':"health_awareness",
    }
    return render(request,"health_awareness.html",d)


def Menstrual_Hygiene(request):
    return render(request,"menstrual_hygiene.html")

def Education(request):
    return render(request,"education.html")


#...................events and pics -13-07-22-......................................

def events(request):
    return render(request,'events.html')

#..................  1  events  .......................
def eventinsert(request):
    return render(request,'eventinsert.html')

def eventsave(request):
    if request.method=='POST':        
        EventName = request.POST['EventName']
        EventDate = request.POST['EventDate']
        EventYear = request.POST['EventYear']
        ei = models.events()
        ei.EventName = EventName
        ei.EventDate = EventDate
        ei.EventYear = EventYear
        ei.save()
        return HttpResponse("succesfully event table inserted and saved")

def events_show(request):
    objects = models.events.objects.all()
    d = {
        'events' : objects,
    }
    return render(request,'events_show.html',d)

def events_edit(request,id):
    objects = models.events.objects.get(id=id)
    d = {
        'events' : objects,
    }
    return render(request,'events_edit.html',d)

def events_update(request):
    if request.method == 'POST':
        ei = models.events.objects.get(id = request.POST['id'])
        ei.EventName = request.POST['EventName']
        ei.EventDate = request.POST['EventDate']
        ei.EventYear = request.POST['EventYear']
        ei.save()
        return redirect(events_show)

def events_delete(request,id):
    objects = models.events.objects.get(id=id)
    objects.delete()
    return redirect(events_show)

#......................   2 events info .............

def event_info(request):
    objs = models.events.objects.all()

    return render(request,'event_info.html',{'events':objs})

def event_info_save(request):
    if request.method=='POST':
        events = request.POST['events']
        #print(events,type(events))
        venue = request.POST['venue']
        address = request.POST['address']
        time = request.POST['time']
        description = request.POST['description']
        print(events)
        obj_events = models.events.objects.get(EventName = events)
        print(obj_events)
        e2 = models.event_info()
        e2.events = obj_events
        e2.venue = venue
        e2.address = address
        e2.time = time
        e2.description = description
        e2.save()        
        return HttpResponse("succesfully event_info table inserted")

def eventinfo_show(request):
    objects = models.event_info.objects.all()
    d = {
        'event_info' : objects,
    }
    return render(request,'eventinfo_show.html',d)

def eventinfo_edit(request,id):
    objects = models.event_info.objects.get(id=id)
    #print(objects.events.EventName)
    event = models.events.objects.get(EventName = objects.events.EventName)
    print(event.EventName)
    d = {
        'event_info' : objects
    }
    return render(request,'eventinfo_edit.html',d)

def eventinfo_update(request):
    if request.method == 'POST':
        e2 = models.event_info.objects.get(id = request.POST['id'])
        # e2.events = request.POST['events']
        e2.events = models.events.objects.get(EventName = request.POST['events'])
        e2.venue = request.POST['venue']
        e2.address = request.POST['address']
        e2.time = request.POST['time']
        e2.description = request.POST['description']
        e2.save() 
        return redirect(eventinfo_show)

def eventinfo_delete(request,id):
    objects = models.event_info.objects.get(id=id)
    objects.delete()
    return redirect(eventinfo_show)

# ........................... 3 images .............................

def event_images(request):
    objs = models.events.objects.all()
    form = ImageForm()
    return render(request,'event_images.html',{'form':form})

def images_save(request):
     if request.method == "POST":
        form = ImageForm(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            #obj = form.instance
            #return render(request,'index.html',{'obj':obj})
            return redirect(images_show)

def images_show(request):
    objects = models.images.objects.all()
    d = {
        'images' : objects,
    }
    return render(request,'images_show.html',d)

def images_edit(request,id):
    objects = models.images.objects.get(id=id)
    d = {
        'images' : objects,
    }
    return render(request,'images_edit.html',d)

def images_update(request):
    if request.method == 'POST':
        e3 = models.images.objects.get(id = request.POST['id'])
        # e3 = models.images()
        # e3.events = models.events.objects.get(EventName = request.POST['events'])
        e3.events = request.POST['events']
        e3.image = request.POST['image']
        e3.date_time = request.POST['date_time']
        e3.save()
        return HttpResponse('images table updated')

def images_delete(request,id):
    objects = models.images.objects.get(id=id)
    objects.delete()
    return HttpResponse('record deleted successfully')



def login(request):
    return render(request,'login.html')