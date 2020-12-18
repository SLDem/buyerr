from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'message-input'}))

    class Meta:
        model = Message
        fields = ('text', )
