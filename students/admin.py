from django.contrib import admin
from .models import Student, Award, Awardship


class StudentInline(admin.TabularInline):
    model = Awardship
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('学生信息', {'fields': ['student_name', 'study_id']}),
        ('学生详情', {'fields': ['student_qq', 'student_email', 'student_tel', 'year_in_school'], 'classes': ['collapse']})
    ]
    inlines = [StudentInline]
    list_display = ('student_name', 'study_id', 'year_in_school')
    search_fields = ['student_name']


class AwardInline(admin.TabularInline):
    model = Awardship
    extra = 1


class AwardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('活动或荣誉名称', {'fields': ['award_name', 'get_time']}),
    ]
    inlines = [AwardInline]
    list_display = ('award_name', 'get_time')


admin.site.register(Student, StudentAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Awardship)
