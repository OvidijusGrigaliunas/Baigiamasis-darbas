from django import forms
from .models import Category
from django.utils.safestring import mark_safe


class RecordForm(forms.Form):
    categories = []
    for category in Category.objects.all():
        categories.append(tuple((category.id, category.category_name)))
    category = forms.ChoiceField(label=mark_safe('Category <br />next line'), widget=forms.Select, choices=categories)
    value = forms.FloatField(label=mark_safe('Value <br />next line'))
