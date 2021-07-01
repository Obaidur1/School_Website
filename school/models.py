from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200,verbose_name="শিরোনাম")
    description = models.TextField(verbose_name="বিস্তারিত")
    notice_file = models.FileField(upload_to="uploads/")
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name = models.CharField(max_length=200,verbose_name="নাম")
    pdsid = models.IntegerField(verbose_name="পিডিএস আইডি")
    basics = models.CharField(max_length=200,verbose_name="মূলপদ")
    title = models.CharField(max_length=200,verbose_name="পদবী")
    date_of_joining = models.DateField(verbose_name="বর্তমান কর্মস্থলে যোগদানের তারিখ")
    mobile_no = models.CharField(max_length=11,verbose_name="মোবাইল নং")
    home_district = models.CharField(max_length=200,verbose_name="নিজ জেলা")
    image = models.FileField(upload_to="uploads/",verbose_name="ছবি")

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name=models.CharField(max_length=100,null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    title=models.CharField(max_length=100)
    image = models.FileField(upload_to="uploads/")
    gallry_id = models.ForeignKey(Gallery,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title


class Staff(models.Model):
    name = models.CharField(max_length=200,verbose_name="নাম")
    title = models.CharField(max_length=200,verbose_name="পদবী")
    date_of_joining = models.DateField(verbose_name="বর্তমান কর্মস্থলে যোগদানের তারিখ")
    mobile_no = models.CharField(max_length=11,verbose_name="মোবাইল নং")
    home_district = models.CharField(max_length=200,verbose_name="নিজ জেলা")
    image = models.FileField(upload_to="uploads/",verbose_name="ছবি")

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=200,verbose_name="নাম")
    no = models.IntegerField(verbose_name="নাম্বার")

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200,verbose_name="নাম")
    roll = models.IntegerField(verbose_name="রোল")
    id_no = models.IntegerField(verbose_name="আইডি")
    class_id = models.ForeignKey(Class,on_delete=models.DO_NOTHING,verbose_name="শ্রেণি")
    image = models.FileField(upload_to="uploads/",verbose_name="ছবি")

    def __str__(self):
        return self.name


class PrincipalImage(models.Model):
    name = models.CharField(max_length=100,verbose_name="নাম")
    image = models.FileField(upload_to="uploads/",verbose_name="ছবি")

    def __str__(self):
        return self.name