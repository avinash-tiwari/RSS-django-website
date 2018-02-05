from django import forms
from subscriptions.models import Websites


class SubForm(forms.ModelForm):
    class Meta():
        model = Websites
        fields = ['web_name','web_url']
