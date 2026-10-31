from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsAdminOrReadOnly
from .permissions import RoleAndOwnerPermission




class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #permission_classes = [IsAdminOrReadOnly]
    permission_classes = [RoleAndOwnerPermission]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)



class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    'message': 'User created successfully',
                    'username': user.username,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
       return Response({
           "message": "Welcome, staff user!"

       })
