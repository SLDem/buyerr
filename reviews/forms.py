from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'review-text-input'}), label='Review')
    pluses = forms.CharField(widget=forms.Textarea(attrs={'class': 'review-pluses-input',
                                                          'placeholder': 'Pluses..'}), label='')
    minuses = forms.CharField(widget=forms.Textarea(attrs={'class': 'review-minuses-input',
                                                           'placeholder': 'Minuses..'}), label='')

    class Meta:
        model = Review
        fields = ('text', 'pluses', 'minuses')