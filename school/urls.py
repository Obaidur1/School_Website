from django.urls import path,include
from .views import *
urlpatterns = [
    path('', index),
    path('notice', allnotice),
    path('notice/<id>', singlenotice),
    path('teachers', teacherlist),
    path('student_list', student_list),
    path('staffs', stafflist),
    path('test', test),
    path('photogalleries', gallerylist),
    path('photogalleries/<id>', galleryphoto),
]
