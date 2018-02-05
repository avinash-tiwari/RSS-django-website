from django import forms
from subscriptions.models import Websites,Feedback


class SubForm(forms.ModelForm):
    class Meta():
        model = Websites
        fields = ['web_name','web_url']

class FeedbackForm(forms.ModelForm):
    class Meta():
        model = Feedback
        fields = ['message']
