from django.contrib import admin

from .models import *

admin.site.site_header="নাজিমখান উচ্চ বিদ্যালয়"
admin.site.site_title="নাজিমখান উচ্চ বিদ্যালয়"

class ImageAdmin(admin.TabularInline):
    model = Photo

class GalleryAdmin(admin.ModelAdmin):
    list_display = ["name","date"]
    list_filter = ["date",]
    inlines = [ImageAdmin,]

class StudentAdmin(admin.ModelAdmin):
    list_display=("name","roll","class_id",)
    list_filter = ('class_id',)
# Register your models here.

admin.site.register(Notice)
admin.site.register(Teacher)
admin.site.register(PrincipalImage)
admin.site.register(Gallery,GalleryAdmin)
admin.site.register(Class)
admin.site.register(Student,StudentAdmin)