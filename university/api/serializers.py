from rest_framework import serializers
from students_app.models import Student
from students_app.models import Author
from students_app.models import Book

class StudentSreializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

