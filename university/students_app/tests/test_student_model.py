import pytest
from students_app.models import Student
from django.utils import timezone

@pytest.mark.django_db
def test_student_model_snapshot(snapshot):
    student = Student.objects.create(
        student_id="STU001",
        name="Ravi Kumar",
        branch="Computer Science",
        age=21,
        email="ravi.kumar@example.com",
        enrolled_date=timezone.now().date()
    )
    
    snapshot.assert_match({
        "student_id": student.student_id,
        "name": student.name,
        "branch": student.branch,
        "age": student.age,
        "email": student.email,
        "enrolled_date": str(student.enrolled_date)
    }, "student_model_snapshot")
