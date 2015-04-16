from django import forms
from euskal.models import User, UserPreferences


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class PreferencesForm(forms.ModelForm):
    fields = []
    for u in User.objects.all().exclude(username='admin'):
        fields.append((u.username, u.username))

    first_left_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))
    second_left_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))
    third_left_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))
    first_right_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))
    second_right_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))
    third_right_choice = forms.CharField(required=False, widget=forms.Select(choices=fields))

    class Meta:
        model = UserPreferences
        exclude = ('user',)