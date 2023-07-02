"""nmf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from organisations import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home',views.home),
     path('',views.home),

    path('about',views.about),
    path('founders',views.founders),
    path('theme',views.theme),
    
    path('Health_Awareness',views.Health_Awareness),
    path('Menstrual_Hygiene',views.Menstrual_Hygiene),
    path('Education',views.Education),

    path('login',views.login),
    

    path('events',views.events),
    
    
    path('eventinsert',views.eventinsert),
    path('eventsave',views.eventsave),
    path('events_show',views.events_show),
    path('events_update',views.events_update,name='events_update'),
    path('events_edit/<int:id>',views.events_edit),
    path('events_delete/<int:id>',views.events_delete),
    
    path('event_info',views.event_info),
    path('event_info_save',views.event_info_save),
    path('eventinfo_show',views.eventinfo_show),
    path('eventinfo_update',views.eventinfo_update,name='eventinfo_update'),
    path('eventinfo_edit/<int:id>',views.eventinfo_edit),
    path('eventinfo_delete/<int:id>',views.eventinfo_delete),

    path('event_images',views.event_images),
    path('images_save',views.images_save), 
    path('images_show',views.images_show,name='images_show'),
    path('images_update',views.images_update,name='images_update'),
    path('images_edit/<int:id>',views.images_edit),
    path('images_delete/<int:id>',views.images_delete),


  
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# imhaes code change here