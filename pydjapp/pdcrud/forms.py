from django import forms

class TaskForm(forms.Form):
	title = forms.CharField(label='Title', required=True)
	description = forms.CharField(label='Description', widget=forms.Textarea, required=True)
	date = forms.DateTimeField(label='Date', widget=forms.SelectDateWidget)
	deadline = forms.DateTimeField(label='Deadline', widget=forms.SelectDateWidget)
	urgent = forms.BooleanField(label='Urgent', required=False)
	important = forms.BooleanField(label='Important', required=False)
