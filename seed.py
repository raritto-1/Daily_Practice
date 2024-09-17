from .models import Department, Student, StudentID
from faker import Faker
import random

fake = Faker()

def generate_unique_student_id():
    while True:
        student_id_value = f"STU-{random.randint(180, 999)}"
        if not StudentID.objects.filter(student_id=student_id_value).exists():
            return student_id_value

        


def seed_db(n=10):
    for _ in range(n):
        # Fetch all departments
        departments_objs = Department.objects.all()
        if not departments_objs:
            continue

        # Randomly select a department
        random_index = random.randint(0, len(departments_objs) - 1)
        department = departments_objs[random_index]

        # Generate a unique student ID
        student_id_value = generate_unique_student_id()
        student_id_obj, created = StudentID.objects.get_or_create(student_id=student_id_value)

        # Generate random student data
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(18, 30)
        student_address = fake.address()

        # Create the student object
        student_obj = Student.objects.create(
            department=department,
            student_id=student_id_obj,  # Assign the StudentID instance
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_address=student_address
        )
