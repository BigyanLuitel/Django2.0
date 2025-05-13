from faker import Faker
fake = Faker()
from .models import *
import random
def create_subjects_marks(n):
    try:
        student_objs= Student.objects.all()
        for student in student_objs:
            subjects= Subject.objects.all()
            for subject in subjects:
                subjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=fake.random_int(min=0, max=100)
                )
    except Exception as e:
        print(f"An error occurred: {e}")

def seed_db(n=10)->None:
    try:
        for _ in range(0, n):
            # Create a new studentID instance
            departments_objs = Department.objects.all()
            random_index = random.randint(0, len(departments_objs) - 1)
            department_obj = departments_objs[random_index]
            student_id = fake.unique.random_int(min=100, max=999)
            student_name = fake.name()
            student_email = fake.email()
            student_address = fake.address()
            student_age = fake.random_int(min=18, max=25)

            student_id_obj = studentID.objects.create(student_id=student_id)
            Student.objects.create(
                Department=department_obj,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_address=student_address,
                student_age=student_age
            )
    except Exception as e:
        print(f"An error occurred: {e}")
