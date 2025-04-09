from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class Student(models.Model):
#     student_id = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     branch = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

# class Author(models.Model):
#     author_id = models.CharField(max_length=100)
#     name = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    
# class Book(models.Model):
#     book_id = models.CharField(max_length=100)
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     genre = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title


class Student(models.Model):
    student_id = models.CharField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    age = models.IntegerField(default=20)
    email = models.EmailField(unique=True, null=True, blank=True)
    enrolled_date = models.DateField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name

class Author(models.Model):
    author_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    book_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13)
    copies = models.IntegerField()

    def __str__(self):
        return self.title

class Course(models.Model):
    course_code = models.CharField(max_length=10)
    title = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField()
    instructor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)
    grade = models.CharField(max_length=2, null=True, blank=True)

class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    head = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    faculty = models.ManyToManyField(User, related_name="departments")
    established_year = models.PositiveIntegerField()

class Library(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    incharge = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    students = models.ManyToManyField(Student)
    total_books = models.IntegerField()

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    attendees = models.ManyToManyField(Student)
    organizer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Assignment(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateField()
    max_marks = models.IntegerField()
    assigned_to = models.ManyToManyField(Student)

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

