from django import forms

class SearchForm(forms.Form):
    searchbox = forms.CharField(label="Enter Search Text",max_length=50 )

