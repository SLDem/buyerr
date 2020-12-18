from django import forms

from .models import Question, Reply


class QuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'question-title-input'}))
    question = forms.CharField(widget=forms.Textarea(attrs={'class': 'question-question-input'}))

    class Meta:
        model = Question
        fields = ('title', 'question', )


class ReplyForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'question-question-input'}), label='')

    class Meta:
        model = Reply
        fields = ('text', )
