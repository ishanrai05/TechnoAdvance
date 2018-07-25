from django import forms
from .models import request_a_workshop

class request_a_workshop(forms.ModelForm):
	class Meta:
		model = request_a_workshop
		fields = [
			'your_name',
			'your_email',
			'conact_number',
			'institute_name',
			'location',
			'designation',
			'workshop',
			'request_date',
			]