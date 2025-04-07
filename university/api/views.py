from students_app.models import Student
from .serializers import StudentSreializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET','POST'])
def studentsView(request):
    if request.method == 'GET':
        # GET ALL THE STUDENT from DB.
        students = Student.objects.all()
        serializer = StudentSreializers(students,many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSreializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)