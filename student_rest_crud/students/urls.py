from django.urls import path
from .views import StudentListAPIView

urlpatterns = [

    path('students/',StudentListAPIView.as_view()),
    path('students/<int:student_id>/',StudentListAPIView.as_view())
]