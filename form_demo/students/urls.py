from django.urls import path
from . import views
urlpatterns = [
    path('search/', views.search_student, name='search_student'),
    path('add/', views.add_student, name='add_student'),
]