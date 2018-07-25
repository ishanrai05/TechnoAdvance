from django.contrib import admin

# Register your models here.
from .models import Upcoming_Event, Workshops, Mail, request_a_workshop, become_a_campus_ambassador_db

admin.site.register(Upcoming_Event)
admin.site.register(Workshops)
admin.site.register(Mail)
admin.site.register(request_a_workshop)
admin.site.register(become_a_campus_ambassador_db)