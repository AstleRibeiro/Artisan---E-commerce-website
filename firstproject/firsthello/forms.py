from django import forms


class FormName(forms.Form):
    email = forms.EmailField()
    fname = forms.CharField()
    lname = forms.CharField()
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
