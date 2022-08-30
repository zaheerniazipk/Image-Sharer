from django import forms


class PostForm(forms.Form):
    # Define form fields here
    image = forms.FileField()
    text = forms.CharField(label='Description')
