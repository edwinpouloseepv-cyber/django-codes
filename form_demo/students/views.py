from django.shortcuts import redirect, render

from .forms import SearchForm, StudentForm


def search_student(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            # Perform search logic here
            # For example, you can query the database for students with the given name
            # and pass the results to the template for rendering.
            return render(request, 'students/search_result.html', {'name': name})
    else:
        form = SearchForm()

    return render(request, 'students/search.html', {'form': form})


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/success.html')  
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {'form': form})



