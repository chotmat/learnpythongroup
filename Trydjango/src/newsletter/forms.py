from django import forms

from .models import SignUp

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()

class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        ### exclude = ['full_name']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain = provider.split('.')
        # if not domain[0] == 'dtu':
        #     raise forms.ValidationError(".")
        if not "edu" in domain:
            raise forms.ValidationError("Please use a valid .edu address")

        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        return full_name