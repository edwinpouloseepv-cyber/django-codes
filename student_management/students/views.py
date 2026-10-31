from django.shortcuts import render, redirect, get_object_or_404
from .models import Student


# View students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})


# Add student
def student_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

        return redirect('student_list')

    return render(request, 'students/student_form.html')


# Update student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.age = request.POST['age']
        student.save()

        return redirect('student_list')

    return render(request, 'students/student_form.html', {'student': student})


# Delete student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()

    return redirect('student_list')
