from rest_framework import serializers
from students_app.models import Student


class StudentSreializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
