from django import forms
from realityquest.models import Mission


class MissionForm(forms.ModelForm):
    lat = forms.CharField(label='Latitud')
    lng = forms.CharField(label='Longitud')
    title = forms.CharField(label='Nombre:')

    class Meta:
        model = Mission
        fields = ('lat', 'lng', 'title')