from django import forms

class ThoughtForm(forms.Form):
    thoughttype = forms.CharField(label='Thought Type', max_length=50, required=True)
    thought = forms.CharField(label='Thought', widget=forms.Textarea, required=True)
    author = forms.CharField(label='Author', max_length=50, required=True)
    date = forms.DateTimeField(label='Date',widget=forms.SelectDateWidget)
