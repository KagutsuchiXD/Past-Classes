from django import forms
from blog.models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), help_text="Comment")
    username = forms.CharField(max_length=30, help_text="Your Username")
    email = forms.CharField(max_length=100,  help_text="Your Email Address")

    class Meta:
        model = Comment
        fields = ['content', 'username', 'email']
