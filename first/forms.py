from django import forms


class Str2WordsForm(forms.Form):
    string = forms.CharField(label='Input string', max_length=100)