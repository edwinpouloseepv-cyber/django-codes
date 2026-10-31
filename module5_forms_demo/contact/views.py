from django.shortcuts import render, redirect
from .forms import ContactMessageForm


def contact(request):

    if request.method == 'POST':

        form = ContactMessageForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('contact_success')

    else:

        form = ContactMessageForm()

    return render(
        request,
        'contact/contact_form.html',
        {'form': form}
    )


def contact_success(request):

    return render(
        request,
        'contact/success.html'
    )