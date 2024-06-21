from django import forms


class SearchForm(forms.Form):
    name = forms.CharField(label='Enter Name: ')