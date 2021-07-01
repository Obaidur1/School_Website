from django import forms
from .models import Photo

class TeacherForm(forms.Form):
    class Meta():
        model = Photo
        fields = ('title','image','gallry_id',)