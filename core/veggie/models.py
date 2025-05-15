from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class recipie(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)
    recepie_name=models.CharField(max_length=100)
    recepie_description=models.TextField()
    recepie_image=models.ImageField(upload_to="recepies/",null=True, blank=True)
    recepie_view_count=models.IntegerField(default=1)


class Department(models.Model):
    department=models.CharField(max_length=100)
    
    def __str__(self):
        return self.department
    class Meta:
        ordering = ['department']
        
        
        
class studentID(models.Model):
    student_id=models.CharField(max_length=100,unique=True)
    
    def __str__(self) -> str:
        return self.student_id
    
    class Meta:
        ordering = ['student_id']
        verbose_name = "Student ID"

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    subject_code=models.CharField(max_length=10,unique=True)
    
    def __str__(self) -> str:
        return self.subject_name
    
    class Meta:
        ordering = ['subject_name']
        verbose_name = "Subject"

class Student(models.Model):
    Department=models.ForeignKey(Department,related_name="depart",on_delete=models.CASCADE)
    student_id=models.OneToOneField(studentID,related_name="student",on_delete=models.CASCADE)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()
    
    
    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "Student"
    
    
class subjectMarks(models.Model):
    student=models.ForeignKey(Student,related_name="student_marks",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,related_name="subject_marks",on_delete=models.CASCADE)
    marks=models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return f"{self.student.student_name} - {self.subject.subject_name}"
    
    class Meta:
        unique_together = ['student', 'subject']
        ordering = ['student']
        verbose_name = "Subject Mark"

class Reportcard(models.Model):
    student=models.ForeignKey(Student,related_name="report_card",on_delete=models.CASCADE)
    student_rank=models.IntegerField(default=0)
    date_of_report_card=models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ['student', 'date_of_report_card']