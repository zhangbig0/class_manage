from django import forms
from students.models import Student


class StudentCreateForm(forms.ModelForm):
    # student_id = forms.CharField(NULL=False, empty_value=False, label='学号')
    # student_name = forms.CharField(label='学号')
    # student_qq = forms.CharField()
    # student_email = forms.CharField()
    # student_tel = forms.CharField()

    class Meta:
        model = Student
        fields = ('student_id', 'student_name', 'student_qq', 'student_email', 'student_tel')

