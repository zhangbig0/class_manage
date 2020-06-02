import time

from django.http import request, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.views.generic.base import View

from .models import Student, Award, Grade


def index(request):
    context = {'student_list': Student, 'Award': Award}
    return render(request, 'students/index.html', context)


# @permission_required('student.can_add', raise_exception=True)
class StudentCreateView(CreateView):
    model = Student
    fields = ('student_id', 'student_name', 'student_qq', 'student_email', 'student_tel')
    template_name = 'students/student_create.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("表单不合法")


class StudentListView(generic.ListView):
    templates = 'students/student_list.html'
    model = Student


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'students/student_detail.html'

    def __get__(self, instance, owner, pk):
        student = Student.objects.get(pk=pk)
        context = {'student', student}
        return render(request, 'students/student_detail.html', context)


class AwardListView(generic.ListView):
    templates = 'students/award_list.html'
    model = Award


def award_detail(request, pk):
    award = get_object_or_404(Award, pk=pk)
    return render(request, 'students/award_detail.html', {'award': award})


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student:student-list')
    template_name = 'students/student_confirm_delete.html'


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('student_id', 'student_name', 'student_qq', 'student_email', 'student_tel')
    template_name = 'students/student_update.html'

    def get_success_url(self):
        return reverse('student:student-detail', kwargs={'pk': self.get_object().pk})


class StudentGradeView(View):
    def get(self, request, pk):
        student = Student.objects.get(pk=pk)
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        grades = Grade.objects.filter(student_id=student.student_id)
        grades_count = grades.count()
        req = request.GET
        res = []
        for grade in grades:
            date = {'course_name': grade.course.course_name, 'grade': grade.grade, 'GPA': grade.GPA, 'semester': grade.semester}
            res.append(date)

        result = {"code": 0, "Msg": "", "count": grades_count, "data": res}
        return JsonResponse(result)
