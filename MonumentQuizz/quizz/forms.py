from django import forms

class MonumentNameForm(forms.Form):
    monument_name = forms.CharField(label='Monument Name', max_length=100)