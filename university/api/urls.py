from django.urls import path
from .import views

urlpatterns = [
   path('students/', views.student_view, name='student-list-create'),
    path('authors/', views.author_view, name='author-list-create'),
    path('books/', views.book_view, name='book-list-create'),
    path('courses/', views.course_view, name='course-list-create'),
    path('enrollments/', views.enrollment_view, name='enrollment-list-create'),
    path('departments/', views.department_view, name='department-list-create'),
    path('libraries/', views.library_view, name='library-list-create'),
    path('events/', views.event_view, name='event-list-create'),
    path('assignments/', views.assignment_view, name='assignment-list-create'),
    path('attendance/', views.attendance_view, name='attendance-list-create'),
]