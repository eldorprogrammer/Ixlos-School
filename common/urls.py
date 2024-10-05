from django.urls import path
from .views import index, contact,courses,events,teachers
urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name="contact"),
    path('courses/',courses,name='courses'),
    path('events/',events,name="events"),
    path('teachers/',teachers,name='teachers'),
]
