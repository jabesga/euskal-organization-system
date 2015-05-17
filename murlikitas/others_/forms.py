from django import forms


class MailForm(forms.Form):
    auth_user = forms.EmailField(max_length=255)
    auth_password = forms.CharField(widget=forms.PasswordInput,)
    mail_subject = forms.CharField(max_length=255)
    mail_message = forms.CharField(max_length=255)
    mail_from = forms.CharField(max_length=255)
    mail_to = forms.EmailField(max_length=255)