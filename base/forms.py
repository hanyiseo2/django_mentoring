from django import forms
from .models import Review

class NewsForm(forms.Form):
    email = forms.EmailField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=('content',)