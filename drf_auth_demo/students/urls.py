from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, RegisterView, AdminOnlyView


router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
]