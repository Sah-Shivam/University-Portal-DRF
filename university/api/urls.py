from django.urls import path
from .import views

urlpatterns = [
    path('students/',views.studentsView),
    path('authors/', views.authorsView),
    path('books/', views.booksView),
]