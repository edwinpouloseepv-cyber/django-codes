from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Task
from .forms import Todoform


# --------------------------
# Student Views (GET CRUD)
# --------------------------

def list_students(request):
    students = Student.objects.all()
    if not students:
        return HttpResponse("No students found.")
    rows = [f"{s.id} - {s.name} {s.email} {s.age}" for s in students]
    return HttpResponse("<br>".join(rows))


def create_student(request):
    name = request.GET.get("name")
    email = request.GET.get("email")
    age = request.GET.get("age")
    
    if not (name and email and age):
        return HttpResponse("Please provide name, email, and age.")
    
    try:
        age = int(age)
    except ValueError:
        return HttpResponse("Age must be an integer.")
        
    student = Student.objects.create(name=name, email=email, age=age)
    return HttpResponse(f"Created student with id={student.id}")


def get_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return HttpResponse(f"{student.id} - {student.name} {student.email} {student.age}")


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    name = request.GET.get("name")
    email = request.GET.get("email")
    age = request.GET.get("age")
    
    if name:
        student.name = name
    if email:
        student.email = email
    if age:
        try:
            student.age = int(age)
        except ValueError:
            return HttpResponse("Age must be an integer.")
            
    student.save()
    return HttpResponse(f"Updated student id={student.id}")


def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return HttpResponse(f"Deleted student id={student_id}")


# --------------------------
# Task Views (POST CRUD)
# --------------------------

def add(request): 
    tasks = Task.objects.all() 
    if request.method == "POST": 
        form = Todoform(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('add') 
    else: 
        form = Todoform() 

    return render(request, 'add.html', {'form': form, 'task1': tasks}) 


def detail(request, id): 
    task = Task.objects.get(id=id) 
    return render(request, 'detail.html', {'task': task}) 


def delete(request, taskid): 
    task = get_object_or_404(Task, id=taskid) 

    if request.method == 'POST': 
        task.delete() 
        return redirect('/') 

    return render(request, 'delete.html', {'task': task}) 


def update(request, id): 
    task = Task.objects.get(id=id) 
    f = Todoform(request.POST or None, instance=task) 
    if f.is_valid(): 
        f.save() 
        return redirect("/") 
    return render(request, "edit.html", {'f': f, 'task': task})