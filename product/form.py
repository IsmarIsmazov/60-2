from django import forms

from product.models import Category, Tag


class ProductFrom(forms.Form):
    name = forms.CharField(max_length=10, min_length=3)
    description = forms.CharField(max_length=1000)
    price = forms.IntegerField()
    photo = forms.ImageField()


class SearchForm(forms.Form):
    ordering = [
        ("created_at", "Created At"),
        ("updated_at", "Updated At"),
        ("price", "Price"),
        ("name", "Name"),
        ("-created_at", "Created At(descinding)"),
        ("-updated_at", "Updated At(descinding)"),
    ]
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    ordering = forms.ChoiceField(choices=ordering, required=False)
    # random = forms.MultipleChoiceField(choices=random_list, required=False)
