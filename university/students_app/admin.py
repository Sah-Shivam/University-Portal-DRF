from django.contrib import admin
from .models import Student 
from .models import Author 
from .models import Book 

admin.site.register(Student)
admin.site.register(Author)
admin.site.register(Book)

# Register your models here.
