from django.contrib import admin
from .models import Student, Award, Awardship


class StudentInline(admin.TabularInline):
    model = Awardship
    extra = 1


class StudentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'study_id']}),
        ('Detail', {'fields': ['year_in_school'], 'classes': ['collapse']})
    ]
    inlines = [StudentInline]
    list_display = ('name', 'study_id', 'year_in_school')
    search_fields = ['student_name']


class AwardInline(admin.TabularInline):
    model = Awardship
    extra = 2


class AwardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'time']}),
        ('Detail', {'fields': ['text']})
    ]
    inlines = [AwardInline]
    list_display = ('name', 'time')


admin.site.register(Student, StudentAdmin)
admin.site.register(Award, AwardAdmin)
