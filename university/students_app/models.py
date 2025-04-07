from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class University(models.Model):
#     name = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#     founded_year = models.IntegerField()
#     accreditation = models.CharField(max_length=255)


# class Department(models.Model):
#     name = models.CharField(max_length=100)
#     head_of_department = models.CharField(max_length=255)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


# class Professor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     qualification = models.CharField(max_length=255)
#     expertise = models.TextField()


# class Course(models.Model):
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, unique=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     professors = models.ManyToManyField(Professor)
#     credits = models.IntegerField()


# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     enrollment_number = models.CharField(max_length=20, unique=True)
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     date_of_birth = models.DateField()
#     courses = models.ManyToManyField(Course)


# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     date_enrolled = models.DateField()
#     status = models.CharField(max_length=50)


# class Marksheet(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     marks = models.IntegerField()
#     term = models.CharField(max_length=20)
#     year = models.IntegerField()  







0