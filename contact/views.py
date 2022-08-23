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
        subject = contact_form.cleaned_data['subject']
        body = {
            'full_name': contact_form.cleaned_data['full_name'],
            'from_email': contact_form.cleaned_data['from_email'],
            'phone': str(contact_form.cleaned_data['phone']),
            'message': contact_form.cleaned_data['message']
            }
        message = "\n".join(body.values())
        try:
            # Django requires the format  send_mail to be ('subject', 'message,'from_email', ['to_email'])
            send_mail(subject, message, 'simpsonjulietc@gmail.com', ['simpsonjulietc@gmail.com'])
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
    