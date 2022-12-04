from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Student, Teacher, Administrator


# Create your views here.

def add_student(reqeust):
    if reqeust.method == "POST":
        first_name = reqeust.POST.get("first_name")
        last_name = reqeust.POST.get("last_name")
        email = reqeust.POST.get("email")
        student_id = reqeust.POST.get("student_id")
        father_name = reqeust.POST.get("father_name")
        mother_name = reqeust.POST.get("mother_name")
        phone_number = reqeust.POST.get("phone_number")

        student = Student(student_id=student_id, phone_number=phone_number, father_name=father_name,
                          mother_name=mother_name)
        student._first_name = first_name
        student._last_name = last_name
        student._email = email

        student.save()

        print("student created successfully")

        return render(reqeust, 'add_student.html')
    else:
        return render(reqeust, 'add_student.html')


def add_teacher(reqeust):
    if reqeust.method == "POST":
        first_name = reqeust.POST.get("first_name")
        last_name = reqeust.POST.get("last_name")
        email = reqeust.POST.get("email")
        teacher_id = reqeust.POST.get("teacher_id")
        join_date = reqeust.POST.get("join_date")

        teacher = Teacher(teacher_id=teacher_id, date_joined=join_date)
        teacher._first_name = first_name
        teacher._last_name = last_name
        teacher._email = email

        teacher.save()

        print("teacher created successfully")

        return render(reqeust, 'add_teacher.html')
    else:
        return render(reqeust, 'add_teacher.html')


def add_administrator(reqeust):
    if reqeust.method == "POST":
        first_name = reqeust.POST.get("first_name")
        last_name = reqeust.POST.get("last_name")
        email = reqeust.POST.get("email")

        administrator = Administrator()
        administrator._first_name = first_name
        administrator._last_name = last_name
        administrator._email = email

        administrator.save()
        return render(reqeust, 'add_administrator.html')
    else:
        return render(reqeust, 'add_administrator.html')
