from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(recipie)
admin.site.register(Department)
admin.site.register(studentID)
admin.site.register(Student)
admin.site.register(Subject)




class subjectMarkAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks')
    search_fields = ('student__student_name', 'subject__subject_name')
    list_filter = ('subject',)
    ordering = ('student', 'subject')

admin.site.register(subjectMarks, subjectMarkAdmin)