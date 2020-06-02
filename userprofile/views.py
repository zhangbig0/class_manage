from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView

from students.models import Student
from .form import UserLoginForm, UserRegisterForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile


def user_login(request):
    if request.method == 'POST':
        user_login_form = UserLoginForm(data=request.POST)
        if user_login_form.is_valid():
            data = user_login_form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return redirect("student:index")

            else:
                return HttpResponse("账号或密码输入有误。请重新输入~")
        else:
            return HttpResponse("账号或密码输入不合法")

    elif request.method == 'GET':
        user_login_form = UserLoginForm()
        context = {'form': user_login_form}
        return render(request, 'userprofile/login.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


def user_logout(request):
    logout(request)
    return redirect("student:index")


def user_register(request):
    if request.method == 'POST':
        user_register_form = UserRegisterForm(data=request.POST)
        if user_register_form.is_valid():
            register_cd = user_register_form.cleaned_data
            user = User.objects.create(username=register_cd['username'],
                                       password=register_cd['password'],
                                       email=register_cd['email'],
                                       )
            student = register_cd['student']
            student.user = user
            user.save()
            student.save()
            login(request, user)
            return redirect("student:index")
        else:
            return HttpResponse("注册表单输入有误,请重新输入~")
    elif request.method == 'GET':
        user_register_form = UserRegisterForm()
        context = {'user_register_form': user_register_form}
        return render(request, 'userprofile/register.html', context)
    else:
        return HttpResponse("请使用GET或POST请求数据")


@login_required(login_url='/userprofile/login/')
def user_delete(request, id):
    user = User.objects.get(id=id)
    if request.user == user:
        logout(request)
        user.delete()
        return redirect("student:index")
    else:
        return HttpResponse("你没有删除操作的权限。")


@login_required(login_url='/userprofile/login')
def student_profile_edit(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        if request.user != user:
            return HttpResponse("你没有权限修改用户信息。")
        user_edit_form = UserEditForm(request.POST, request.FILES)
        print(user_edit_form)
        if user_edit_form.is_valid():
            user_data = user_edit_form.cleaned_data
            user.email = user_data['email']

            if Profile.objects.filter(user_id=id).exists():
                profile = Profile.objects.get(user_id=id)
            else:
                profile = Profile.objects.create(user=user)

            if 'avatar' in request.FILES:
                profile.avatar = user_data['avatar']
            profile.bio = user_data['bio']

            student = user_data['student']
            old_student = user.student
            old_student.user = None
            old_student.save(update_fields=['user'])

            student.user = user

            profile.save(update_fields=['avatar', 'bio'])
            user.save(update_fields=['email'])
            student.save(update_fields=['user'])

            return redirect("userprofile:student-profile-edit", id)
        else:
            return HttpResponse('编辑表单输入有误，请重新输入！')

    elif request.method == 'GET':

        user_edit_form = UserEditForm()
        context = {
            'user_edit_form': user_edit_form,
            'user': user,
            'students': Student.objects.all()
        }
        return render(request, 'userprofile/edit.html', context)
    else:
        return HttpResponse('请使用GET或者POST请求数据')

# class UserUpdateView(UpdateView):
#     model = User
#     template_name = 'userprofile/edit.html'
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'userprofile/edit.html', self.get_context_data())
#
#     def post(self, request, *args, **kwargs):
#         profile_form = ProfileEditForm(data=request.POST)
#         user_form = UserUpdateView(data=request.POST)
#
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user_edit_form = UserEditForm()
#         profile_edit_form = ProfileEditForm()
#         context['user_edit_form'] = user_edit_form
#         context['profile_edit_form'] = profile_edit_form
#         return context
