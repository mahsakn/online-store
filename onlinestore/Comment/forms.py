from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import Textarea, TextInput

from .models import CommentMe


class Comment(forms.Form):
    comment = forms.CharField(
        max_length=1024,
        widget=forms.TextInput(
            attrs={'class': 'e-field-inner'}
        )
    )
    emaill = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={'class': 'e-field-inner', 'readonly': 'readonly'}
        )
    )
