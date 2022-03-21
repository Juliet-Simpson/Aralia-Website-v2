from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm



def contact(request):
    """ A view to return the contact form page """

    if request.method == 'GET':
        contact_form = ContactForm()
    else:
        contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        full_name = contact_form.cleaned_data['full_name']
        subject = contact_form.cleaned_data['subject']
        from_email = contact_form.cleaned_data['from_email']
        message = contact_form.cleaned_data['message']
        try:
            # send_mail(subject, message, from_email, ['sales@aralia.co.uk'])
            send_mail(subject, message, from_email, ['simpsonjulietc@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')

    template = 'contact/contactform.html'
    context = {
        'contact_form': contact_form,
    }

    return render(request, template, context)


def success(request):
    """ A view to return the success page """

    return render(request, 'contact/success.html')
    