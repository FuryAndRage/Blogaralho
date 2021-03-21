from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms

class PostForm(forms.Form):
    post_content = forms.CharField(widget=SummernoteWidget())  # instead of forms.Textarea