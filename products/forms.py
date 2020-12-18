from django import forms
from .models import Category, Product, Image, SubCategory


class CategoryForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'style': 'margin-top: 10px;'}), label='')

    class Meta:
        model = Category
        fields = ('title', 'image')


class ProductForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'product-title-input'}), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'product-description-input'}), required=False)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'product-quantity-input'}), required=True)
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'product-quantity-input'}), label='Price($)', required=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'category', 'sub_category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sub_category'].queryset = SubCategory.objects.none()
        self.fields['category'].required = True

        if 'category' in self.data:
            try:
                category = int(self.data.get('category'))
                self.fields['sub_category'].queryset = SubCategory.objects.filter(category=category).order_by('title')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['sub_category'].queryset = self.instance.category.subcategories.order_by('title')


class ImagesForm(forms.ModelForm):
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'product-image-input', 'multiple': True}),
                             required=False)

    class Meta:
        model = Image
        fields = ('images', )
