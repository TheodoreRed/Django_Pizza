from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    name = forms.CharField(error_messages={"required": "Pizza Place Name & Location"})
    rating = forms.IntegerField(error_messages={"required": "(1-10)"})

    class Meta:
        model = Pizza
        fields = "__all__"
