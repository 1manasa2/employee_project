from django import forms
from .models import BlogPost
class BlogPostForm(forms.Form):
    title =  forms.CharField(max_length=200)
    body = forms.CharField(max_length=200)
    # class Meta:
    #     model=BlogPost
        # fields='__all__'