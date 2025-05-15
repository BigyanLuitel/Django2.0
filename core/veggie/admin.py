from django.contrib import admin
from django.db.models import Sum
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
from django.db.models import Sum

class ReportcardAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_student_rank', 'get_total_marks', 'date_of_report_card')

    def get_total_marks(self, obj):
        total = subjectMarks.objects.filter(student=obj.student).aggregate(
            total=Sum('marks')
        )['total']
        return total or 0
    get_total_marks.short_description = 'Total Marks'

    def get_student_rank(self, obj):
        student_id = obj.student.student_id.student_id
        # Get all students with their total marks
        ranks = Student.objects.annotate(
            total=Sum('student_marks__marks')
        ).order_by('-total', '-student_age')  # descending order

        # Loop through the ranked list, starting index at 1
        for i, student in enumerate(ranks, start=1):
            if student.student_id.student_id == student_id:
                return i
        return '-'
    get_student_rank.short_description = 'Rank'


admin.site.register(subjectMarks, subjectMarkAdmin)
admin.site.register(Reportcard, ReportcardAdmin)
