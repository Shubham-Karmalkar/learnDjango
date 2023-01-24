from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget= forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "first_class second_class",
            "id": "my_id",
            "rows": 15,
            "cols": 150
        }
    ))
    price = forms.DecimalField(initial=249.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "CFE" not in title:
            raise forms.ValidationError("Title is not Valid")
        return title


class RawProductForm(forms.Form):
    # required for all field is by default True
    title = forms.CharField(label='', widget= forms.TextInput(attrs={"placeholder":"Your Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "class": "first_class second_class",
            "id": "my_id",
            "rows": 15,
            "cols": 150
        }
    ))
    price = forms.DecimalField(initial=249.99)

