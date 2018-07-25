from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from datetime import datetime
from .models import Upcoming_Event, Workshops, Mail, request_a_workshop, become_a_campus_ambassador_db
from .forms import MailForm, request_a_workshop_form
from django.contrib import messages
# Create your views here.

def index(request):
	
	now = timezone.now()
	upcoming_event = Upcoming_Event.objects.order_by('-date')
	workshop = Workshops.objects.order_by('-date')
	context = {
				'upcoming_events':upcoming_event,
				'workshops': workshop,
			}
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	return render(request, 'techx/index.html', context)
	pass


# Create your views here.

def upcoming_events(request,id):
	upcoming_event = Upcoming_Event.objects.get(pk=id)
	context = {
				'upcoming_events':upcoming_event,
				'workshops': workshop,
			}
	
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	return render(request, 'upcoming_events.html', context)

def upcoming_events_temporary(request):
	return render(request, 'upcoming_events.html', {})
	
def workshops(request,id):
	workshops = Workshops.objects.get(pk=id)
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
				
			}						
	return render(request, 'workshops.html', context)

def about(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	return render (request,'about.html',{})

def workshop(request):
	workshop = Workshops.objects.order_by('-date')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops': workshop,
						}

	return render(request, 'workshop.html', context)
	pass


def android(request):
	workshops = Workshops.objects.get(workshop_title='Android App Development')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)

def BridgeDesign(request):
	workshops = Workshops.objects.get(workshop_title='Bridge Design')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)

def EthicalHacking(request):
	workshops = Workshops.objects.get(workshop_title='Ethical Hacking')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)

def IoT(request):
	workshops = Workshops.objects.get(workshop_title='Internet of Things')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)



def digital(request):
	workshops = Workshops.objects.get(workshop_title='Digital Marketing')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)


def cloudComputing(request):
	workshops = Workshops.objects.get(workshop_title='Cloud Computing')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)


def ml(request):
	workshops = Workshops.objects.get(workshop_title='Machine Learning')
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		print (name, email, message, contact_number)
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	context = {
				'workshops':workshops,
			}						
	return render(request, 'workshops.html', context)

def request_a_workshop_view(request):
	workshop = Workshops.objects.order_by('workshop_title')
	context = {
				
				'workshops': workshop,
			}
	
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		contact_number = request.POST.get("contact_number")
		institute_name = request.POST.get("institute")
		location = request.POST.get("location")
		designation = request.POST.get("designation")
		workshop = request.POST.get("workshop")
		request_date = request.POST.get("request_date")
		request_a_workshop_ = request_a_workshop()
		request_a_workshop_.your_name = name
		request_a_workshop_.your_email = email
		request_a_workshop_.contact_number = contact_number
		request_a_workshop_.institute_name = institute_name
		request_a_workshop_.location = location
		request_a_workshop_.designation = designation
		request_a_workshop_.workshop = workshop
		request_a_workshop_.request_date = request_date
		request_a_workshop_.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')

	return render(request, 'request_a_workshop.html', context)
	pass
def contact_us(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		message = request.POST.get("message")
		contact_number = request.POST.get("contact_number")
		mail = Mail()
		mail.your_name = name
		mail.your_email = email
		mail.contact_number = contact_number
		mail.your_content = message
		mail.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	return render(request, 'contact_us.html', {})
	pass

def become_a_campus_ambassador(request):
	if request.method == "POST":
		name = request.POST.get("name")
		email = request.POST.get("email")
		contact_number = request.POST.get("contact_number")
		college = request.POST.get("college")
		department = request.POST.get("department")
		city = request.POST.get("city")
		graduating_year = request.POST.get("graduating_year")
		permanent_address = request.POST.get("permanent_address")
		past_experience = request.POST.get("past_experience")
		become_a_campus_ambassador_object=become_a_campus_ambassador_db()
		become_a_campus_ambassador_object.your_name = name
		become_a_campus_ambassador_object.your_email = email
		become_a_campus_ambassador_object.contact_number = contact_number
		become_a_campus_ambassador_object.college_name = college
		become_a_campus_ambassador_object.department = department
		become_a_campus_ambassador_object.city = city
		become_a_campus_ambassador_object.graduating_year = graduating_year
		become_a_campus_ambassador_object.permanent_address = permanent_address
		become_a_campus_ambassador_object.past_experience = past_experience
		become_a_campus_ambassador_object.save()
		messages.success(request, "new Item created")
		return render(request , 'thankyou.html')
	return render(request, 'become_a_campus_ambassador.html', {})
	pass

def laptop(request):
	return render(request,'laptop.html',{})