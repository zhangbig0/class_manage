from django.shortcuts import render
from django.http import HttpResponseRedirect, request, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.template import loader

from .models import Student, Award, Awardship


def index(request):
    context = {'student_list': Student, 'Award': Award}
    return render(request, 'students/index.html', context)


class StudentListView(generic.ListView):
    templates = 'students/student_list.html'
    model = Student


def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})


class AwardListView(generic.ListView):
    templates = 'students/award_list.html'
    model = Award


def award_detail(request, award_id):
    award = get_object_or_404(Award, id=award_id)
    return render(request, 'students/award_detail.html', {'award': award})
