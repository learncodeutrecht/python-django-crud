from django import forms


class ThoughtForm(forms.Form):
    title = forms.CharField(label='Title',max_length=60, required=True)
    thought = forms.CharField(label='Thought', widget=forms.Textarea, required=True)
