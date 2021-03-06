# sendemail/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.forms.utils import ErrorList


def only_int(value): 
    """Custom Validation error"""

    if value.isdigit() is False:
        raise ValidationError('Phone Number cannot contain letters')


class ContactForm(forms.Form):
    """ Contact form fields """

    full_name = forms.CharField(required=True, max_length=50)
    from_email = forms.EmailField(required=True, max_length=254)
    phone = forms.CharField(validators=[only_int], required=False, max_length=16)
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


class DivErrorList(ErrorList):
    """docstring"""
    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        """docstring"""
        if not self: 
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(['<div class="error">%s</div>' % e for e in self])


f = ContactForm(auto_id=False, error_class=DivErrorList)
f.as_p()