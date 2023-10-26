from django import forms


class BuyProductForm(forms.Form):
    color = forms.CharField(
        widget=forms.TextInput(attrs={"data-toggle": "collapse", "data-target": "#{{ code.color_name }}"})
    )
    size = forms.CharField()
    quantity = forms.IntegerField()
