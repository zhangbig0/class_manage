from django.urls import path

from .views import index, StudentDetailView, StudentCreateView, AwardListView, StudentDeleteView, StudentUpdateView, StudentGradeView, StudentListView

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('student_list/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('award_list/', AwardListView.as_view(), name='award-list'),
    path('award_list/<int:pk>/', StudentDetailView.as_view(), name='award-detail'),
    path('student_list/create/', StudentCreateView.as_view(), name='student-create'),
    path('student_list/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('student_list/<int:pk>/update', StudentUpdateView.as_view(), name='student-update'),
    path('grade/<int:pk>/', StudentGradeView.as_view(), name='student-grade'),
]
