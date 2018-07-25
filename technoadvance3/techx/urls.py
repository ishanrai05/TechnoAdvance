from django.conf.urls import url, include
from . import views
app_name = 'techno'
urlpatterns = [
    url(r'workshops/BridgeDesign/$',views.BridgeDesign,name='BridgeDesign'),
	url(r'workshops/EthicalHacking/$',views.EthicalHacking,name='EthicalHacking'),
	url(r'workshops/Android/$',views.android,name='Android App Development'),
	url(r'workshops/IoT/$',views.IoT,name='IoT'),
	url(r'workshops/Digital/$',views.digital,name='Digital Marketing'),
	url(r'workshops/ML/$',views.ml,name='Machine Learning'),
	url(r'workshops/CloudComputing/$',views.cloudComputing,name='CloudComputing'),
	url(r'workshops/(?P<id>[0-9]+)/$',views.workshops,name='workshops'),
	url(r'upcoming_events/(?P<id>[0-9]+)/$',views.upcoming_events,name='upcoming'),
	url(r'^request_a_workshop/$',views.request_a_workshop_view,name='request_a_workshop_view'),
	url(r'^upcoming_events_temporary/$',views.upcoming_events_temporary,name='upcoming_events_temporary'),	
	url(r'^become_a_campus_ambassador/$',views.become_a_campus_ambassador,name='become_a_campus_ambassador'),
	url(r'^about/$',views.about,name='about'),
	url(r'^workshop/$',views.workshop,name='workshop'),
	url(r'^contact_us/$',views.contact_us,name='contact_us'),
    url(r'^$',views.index,name='index'),

]
#become_a_campus_ambassador