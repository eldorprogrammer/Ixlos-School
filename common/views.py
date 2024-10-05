from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request=request, template_name="blog/index.html")

def contact(requset):
    return render(request=requset, template_name='blog/contact.html')

def courses(request):
    return render(request=request, template_name='blog/courses.html')

def events(request):
    return render(request=request, template_name="blog/events.html")

def teachers(request):
    return render(request=request, template_name="blog/teachers.html")



