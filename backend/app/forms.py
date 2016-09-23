from django import forms

class Myform(forms.Form):
	word = forms.CharField(max_length=100)
