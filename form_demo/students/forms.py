from django import forms
from students.models import Student
class SearchForm(forms.Form):
    name = forms.CharField(
        label="student Name"
    )

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email','age']