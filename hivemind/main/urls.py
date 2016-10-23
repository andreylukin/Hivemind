from django.conf.urls import url

from . import views

app_name = 'main'

urlpatterns = [
	#main/addClassUser/3/6/
    url(r'^addClassUser/(?P<user>[1-9][0-9]*)/(?P<classes>[1-9][0-9]*)$', views.addClassUser, name='addClassUser'),

	#main/getallbuildinglocations/
    url(r'^getallbuildinglocations/$', views.getAllBuildingLocations, name='getAllBuildingLocations'),

	#main/getsessions/3/
    url(r'^getsessions/(?P<classesneeded>[1-9][0-9]*)/$', views.getSessions, name='getSessions'),

	#main/addUserClasses/3/
    url(r'^getUserClasses/(?P<user>[1-9][0-9]*)/$', views.getUserClasses, name='getUserClasses'),

	#main/createNewSession/3/6/8/
    url(r'^createNewSession/(?P<user>[1-9][0-9]*)/(?P<building>[1-9][0-9]*)/(?P<classes>[1-9][0-9]*)/$', views.createNewSession, name='createNewSession'),

	#main/joinSession/3/6/
    url(r'^joinSession/(?P<user>[1-9][0-9]*)/(?P<session>[1-9][0-9]*)/$', views.joinSession, name='joinSession'),

	#main/leaveSession/3/6/
    url(r'^leaveSession/(?P<user>[1-9][0-9]*)/(?P<session>[1-9][0-9]*)/$', views.leaveSession, name='leaveSession'),

	#main/nameEntity/3/
    url(r'^nameEntity/(?P<user>[1-9][0-9]*)/$', views.nameEntity, name='nameEntity'),

	#main/nameBuilding/3/
    url(r'^nameBuilding/(?P<building>[1-9][0-9]*)/$', views.nameBuilding, name='nameBuilding'),

	#main/nameClass/3/
    url(r'^nameClass/(?P<classes>[1-9][0-9]*)/$', views.nameClass, name='nameClass'),

	#main/honeyEntity/3/
    url(r'^honeyEntity/(?P<user>[1-9][0-9]*)/$', views.honeyEntity, name='honeyEntity'),

	#main/honeyAllEntity/
    url(r'^honeyAllEntity/$', views.honeyAllEntity, name='honeyAllEntity'),
]
