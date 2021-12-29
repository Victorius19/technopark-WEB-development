from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter you username here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter you password here'}))

class QuestionForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment title', 'maxlength': '50'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'maxlength': '500', 'rows': '3'}))
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tags must be separated by commas', 'maxlength': '100'}))

    def clean_tags(self):
        if self.cleaned_data['tags'].isalpha() == False:
            self.add_error(None, "Tags can only consist of letters of the English alphabet.")

        return self.cleaned_data['tags']

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter you username here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter you password here'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat you password here'}))
    nickname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter you nickname here'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter you nickname here'}))

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['password'] != cleaned_data['repeat_password']:
            self.add_error(None, "Password do not match.")

        return cleaned_data

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment here', 'maxlength': '500', 'style': 'height: 150px'}))
    question_id = forms.IntegerField(widget=forms.HiddenInput())