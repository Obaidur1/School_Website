from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import *

from .forms import TeacherForm

def index(request):
    notices = Notice.objects.all().order_by('-id')[0:10]
    return render(request,"index.html",{"notics":notices})


def allnotice(request):
    notices = Notice.objects.all().order_by('-id')
    return render(request,"allnotice.html",{"notics":notices})


def singlenotice(request,id):
    notice = get_object_or_404(Notice,id=id)
    return render(request,"singlenotice.html",{"notice":notice})

def teacherlist(request):
    teachers = Teacher.objects.all()
    return render(request,"teacherlist.html",{"teachers":teachers})

def stafflist(request):
    staffs = Staff.objects.all()
    return render(request,"stafflist.html",{"staffs":staffs})


def gallerylist(request):
    g  = Gallery.objects.all().order_by('-date')
    return render(request,"photogallery.html",{"galleries":g})


def galleryphoto(request,id):
    photos = get_list_or_404(Photo,gallry_id=id)
    #photos = Photo.objects.all().filter(gallry_id=id)
    gallery = get_object_or_404(Gallery,id=id)
    return render(request,"singlegallery.html",{"photos":photos,"Gallery":gallery})

def student_list(request):
    classess = Class.objects.all()
    students = None
    if(request.POST):
        try:
            class_id = request.POST.get('class')
            students = Student.objects.filter(class_id = class_id)
        except:
            pass

    return render(request,"student_list.html",{"classess":classess,"students":students})


def test(request):
    form = TeacherForm()
    return render(request,"test.html",{"form":form})