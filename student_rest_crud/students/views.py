from urllib import request
from .serializers import StudentSerializer
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student



class StudentListAPIView(APIView):
    # def post(self, request): #request object
    #     serializer = StudentSerializer(data=request.data) #request data is the json data sent by client
    #     if serializer.is_valid(): #serialize the data and check if it is valid
    #         serializer.save() #json data is saved to the database and returned as a response
    #         return Response(serializer.data)
    #     return Response(serializer.errors) #if the json data is not valid, return the errors
    def post(self, request):

        is_bulk = isinstance(request.data, list)
        serializer = StudentSerializer(
            data=request.data,
            many=is_bulk
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
            serializer.data,
            status=201
            )

        return Response(serializer.errors, status=400)


    # def get(self, request):
    #     students = Student.objects.all() #Student model is used to get all the students from the database
    #     serializer = StudentSerializer(students, many=True) #serializes the collection of students and returns response
    #     return Response(serializer.data)

    # def get_student(self, student_id):
    #     return Student.objects.get(id=student_id)

    # def get(self, request, student_id):
    #     student = self.get_student(student_id)
    #     serializer = StudentSerializer(student)
    #     return Response(serializer.data)

    def get(self, request, student_id=None):

        # If student_id is provided, get one student
        if student_id is not None:
            student = get_object_or_404(
                Student,
                id=student_id
            )
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        # Otherwise, get all students
        students = Student.objects.all()

        # Filter students by age if age is provided
        age = request.query_params.get('age')

        if age:
            students = students.filter(age=age)

        search = request.query_params.get('search')

        if search:
            students = students.filter(name__icontains=search) | students.filter(email__icontains=search)
            # students=students.filter(Q(name__icontains=search) & Q(email__icontains=search))

        # Ordering
        ordering = request.query_params.get('ordering')
        if ordering in ['name', '-name', 'age', '-age']:
            students = students.order_by(ordering)


        # serializer = StudentSerializer(
        #     students,
        #     many=True
        # )

        # return Response(serializer.data)

        # Divide results into pages
        paginator = PageNumberPagination()
        paginator.page_size = 25

        page = paginator.paginate_queryset(
        students, request, view=self
        )
        # Convert the current page into JSON
        serializer = StudentSerializer(page, many=True)
        #  Return paginated JSON
        return paginator.get_paginated_response(serializer.data)



    def put(self, request, student_id):

        student = self.get_student(student_id)

        serializer = StudentSerializer( # existing student data and new data from the request are passed to the serializer
            student,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, student_id):
        student = self.get_student(student_id)
        student.delete()
        return Response({
        "message": "Student deleted successfully"
        })

    def get_filtered_students(self, request):
        age = request.query_params.get('age')
        if age:
            students = Student.objects.filter(age=age)
        else:
            students = Student.objects.all()
        return students
