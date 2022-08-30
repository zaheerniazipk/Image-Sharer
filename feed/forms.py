from django import forms


class PostForm(forms.Form):
    # Define form fields here
    text = forms.CharField()
    image = forms.FileField()
