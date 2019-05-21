from django.urls import path
from .views import StudentListView, AwardListView
from . import views

app_name = 'student'
urlpatterns = [
    path('', views.index, name='index'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('student_list/<int:student_id>/', views.student_detail, name='student-detail'),
    path('award_list/', AwardListView.as_view(), name='award-list'),
    path('award_list/<int:award_id>/', views.award_detail, name='award-detail'),
]
