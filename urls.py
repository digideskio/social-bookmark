import os
from django.conf.urls.defaults import *
from bookmarks.views import *
from django.views.generic.simple import direct_to_template

site_media = os.path.join( os.path.dirname(os.path.abspath(__file__)), 'site_media' )

urlpatterns = patterns('',
     (r'^$', main_page ),
     (r'^user/(\w+)/$', user_page),
     (r'^login/$', 'django.contrib.auth.views.login'),
     (r'^logout/$', logout_page ),
	 (r'^site_media/(?P<path>.*)$','django.views.static.serve',
		{'document_root': site_media}),
	 (r'^register/$', register_page),
	 (r'^register/success/$', direct_to_template,
		{'template': 'registration/register_success.html'}),
)