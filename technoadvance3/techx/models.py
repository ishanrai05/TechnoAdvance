from django.db import models
from datetime import datetime
# Create your models here.
class Upcoming_Event(models.Model):
	event_date = models.DateTimeField()
	event_title = models.CharField(max_length = 200)
	event_detail = models.TextField()
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.event_title

class Workshops(models.Model):
	workshop_title = models.CharField(max_length = 200)
	workshop_about = models.TextField(null=True)
	workshop_details = models.TextField(null=True)
	workshop_requirements = models.TextField(null=True)
	workshop_benefits = models.TextField(null=True)
	workshop_image = models.FileField(null = True, blank = True)
	date = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.workshop_title
	
class Mail(models.Model):
	your_name = models.CharField(max_length=1000)
	your_email = models.EmailField(max_length=254)
	contact_number = models.CharField(max_length=1000)
	your_content = models.TextField(max_length=5000)
	mailed_date = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.subject

class request_a_workshop(models.Model):
	your_name = models.CharField(max_length=100, null=True)
	your_email = models.EmailField(max_length=254, null=True)
	contact_number = models.CharField(max_length=100, null=True)
	institute_name = models.TextField(max_length=500, null=True)
	location = models.TextField(max_length=100, null=True)
	designation = models.TextField(max_length=100, null=True)
	workshop =  models.TextField(max_length=100, null=True)
	request_date = models.DateTimeField(default=datetime.now)
	def __str__(self):
		return self.your_name

class become_a_campus_ambassador_db(models.Model):
	your_name = models.CharField(max_length=100, null=True)
	your_email = models.EmailField(max_length=254, null=True)
	contact_number = models.CharField(max_length=100, null=True)
	college_name = models.CharField(max_length=500, null=True)
	department = models.CharField(max_length=100, null=True)
	city = models.CharField(max_length=100, null=True)
	graduating_year = models.CharField(max_length=100, null=True)
	permanent_address = models.TextField(null=True)
	past_experience =  models.TextField(null=True)
	request_date = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.your_name