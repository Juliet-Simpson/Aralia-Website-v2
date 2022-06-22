# sendemail/forms.py
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.Form):
    """ Contact form fields """

    full_name = forms.CharField(required=True, max_length=50)
    from_email = forms.EmailField(required=True, max_length=254)
    phone = PhoneNumberField(required=False, max_length=13)
    subject = forms.CharField(required=False, max_length=254)
    message = forms.CharField(widget=forms.Textarea, required=True, max_length=2000)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'from_email': 'Email Address',
            'subject': 'Subject',
            'phone': 'Phone Number',
            'message': 'Message',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'my_form'
            self.fields[field].label = False