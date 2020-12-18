from django import forms

from products.models import Product


class SearchForm(forms.ModelForm):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search'}), label='')
    is_available = forms.BooleanField(required=False)
    max_price = forms.IntegerField(widget=forms.NumberInput, required=False)
    min_price = forms.IntegerField(widget=forms.NumberInput, required=False)

    class Meta:
        model = Product
        fields = ['query', 'category']

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
