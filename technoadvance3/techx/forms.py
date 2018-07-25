from django import forms 
from .models import Mail, request_a_workshop


class MailForm(forms.ModelForm):
	your_name = forms.CharField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder':'Enter your name',
			'data-rule':"minlen:4", 
			'data-msg':"Please enter at least 4 chars",
		}
	))
	class Meta:
		model = Mail 
		fields = [
			'your_name',
			'your_email',
			'contact_number',
			'your_content',
			]

class request_a_workshop_form(forms.ModelForm):
	your_name = forms.CharField(widget = forms.TextInput(
		attrs={
			'class':'form-control',
			'placeholder':'Enter your name',
			'data-rule':"minlen:4", 
			'data-msg':"Please enter at least 4 chars",
		
		}
	))
	class Meta:
		model = request_a_workshop
		fields = [
			'your_name',
			'your_email',
			'contact_number',
			'institute_name',
			'location',
			'designation',
			'workshop',
			'request_date',
			]