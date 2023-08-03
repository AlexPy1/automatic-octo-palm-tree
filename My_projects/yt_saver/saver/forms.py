from django import forms


class PostForm(forms.Form):
    v_url = forms.CharField(label='url')
