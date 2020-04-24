from django import forms

class TextForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), max_length=512)