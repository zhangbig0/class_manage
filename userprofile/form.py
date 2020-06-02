from django import forms
from django.contrib.auth.models import User
from students.models import Student
from userprofile.models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='再次输入密码', widget=forms.PasswordInput())
    student = forms.ModelChoiceField(queryset=Student.objects.all(), help_text='绑定学生', label='学生')

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            return forms.ValidationError("密码输入不一致，请重试。")


class UserEditForm(forms.ModelForm):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), label='学生')
    avatar = forms.ImageField(required=False)
    bio = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ['email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
