from django import forms

class CommentForm(forms.Form):
	email = forms.EmailField(max_length=254, help_text='')
	username = forms.CharField(max_length = 100, help_text='')
	comment = forms.CharField(widget=forms.Textarea)