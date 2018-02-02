from django import forms
from app1.models import Subscriptions


class SubForm(forms.ModelForm):
    class Meta():
        model = Subscriptions
        fields = '__all__'
