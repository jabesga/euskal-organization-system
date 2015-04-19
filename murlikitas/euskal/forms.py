# -*- encoding: utf-8 -*-
from django import forms
from euskal.models import User, UserPreferences, Choices, Option


class UserForm(forms.ModelForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    first_name = forms.CharField(label='Nombre:')
    last_name = forms.CharField(label='Primer apellido:')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')


class ChoicesForm(forms.ModelForm):

    first_choice = forms.CharField(initial='',
                                   required=False,
                                   label='Primera opcion',
                                   max_length=128,
                                   widget=forms.Select(choices=[('','')]))
    second_choice = forms.CharField(initial='',
                                    required=False,
                                    label='Segunda opcion',
                                    max_length=128,
                                    widget=forms.Select(choices=[('','')]))
    third_choice = forms.CharField(initial='',
                                   required=False,
                                   label='Tercera opcion',
                                   max_length=128,
                                   widget=forms.Select(choices=[('','')]))

    class Meta:
        model = Choices
        fields = ('first_choice', 'second_choice', 'third_choice')

    def __init__(self, *args, **kwargs):
        self.up = kwargs.pop('up')
        self.prefix = kwargs.get('prefix')
        super(ChoicesForm, self).__init__(*args, **kwargs)

        full_name_list = [('', '')]
        queryset = User.objects.all().exclude(username='admin')
        for user in queryset:
            full_name = "%s %s" % (user.first_name, user.last_name)
            full_name_list.append((full_name, full_name))
        full_name_list = sorted(full_name_list)

        self.fields['first_choice'].widget = forms.Select(choices=full_name_list)
        self.fields['second_choice'].widget = forms.Select(choices=full_name_list)
        self.fields['third_choice'].widget = forms.Select(choices=full_name_list)

        try:
            upref = UserPreferences.objects.get(user_profile=self.up)

            if self.prefix == 'left':
                self.fields['first_choice'].initial = upref.left_choices.first_choice
                self.fields['second_choice'].initial = upref.left_choices.second_choice
                self.fields['third_choice'].initial = upref.left_choices.third_choice
            elif self.prefix == 'right':
                self.fields['first_choice'].initial = upref.right_choices.first_choice
                self.fields['second_choice'].initial = upref.right_choices.second_choice
                self.fields['third_choice'].initial = upref.right_choices.third_choice

        except UserPreferences.DoesNotExist:
            pass


class OptionsForm(forms.Form):

    name_choice = forms.ChoiceField(label='', choices=[('', '')], widget=forms.RadioSelect())

    def __init__(self, *args, **kwargs):
        super(OptionsForm, self).__init__(*args, **kwargs)

        option_name_list = []
        queryset = Option.objects.all()
        for option in queryset:
            option_name_list.append((option.option_name, option.option_name))
        option_name_list = sorted(option_name_list)

        self.fields['name_choice'].choices = option_name_list


class NewOptionForm(forms.ModelForm):

    option_name = forms.CharField(label='Añadir nuevo nombre',max_length=128)

    class Meta:
        model = Option
        fields = ['option_name']

