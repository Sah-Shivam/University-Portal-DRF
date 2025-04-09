from django.contrib import admin
from .models import Student 
from .models import Author 
from .models import Book 
from .models import (
    Student, Author, Book, Course, Enrollment, Department,
    Library, Event, Assignment, Attendance
)

admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Department)
admin.site.register(Library)
admin.site.register(Event)
admin.site.register(Assignment)
admin.site.register(Attendance)
# Register your models here.
