from django import forms
from someapp import models

class CommentForm(forms.ModelForm):
    class Meta:
        model=models.Comments
        fields=["username","content","author"]
        exclude=["author"]


class FileForm(forms.Form):
    document=forms.FileField()
    test=forms.CharField(widget=forms.PasswordInput)




