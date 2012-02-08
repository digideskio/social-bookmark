# View for the bookmark application
# Author: @sarat - csarath@gmail.com
# Date: 15-Jul-2011

from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.template import RequestContext

#generate the main page content
def main_page(request) :
    #variables = Context({
	#	'head_title': u'Django Bookmarks',
	#	'page_body': u'Where you can store and share bookmarks!',
    #    'user': request.user
	#})
    
	#variables.update(csrf(request))
    return render_to_response( 'main_page.html',RequestContext(request))

# Context is a object which can take Python Dictionary elements in the constructor)

# generate the user page content
def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		raise Http404(u'Requested user not found');

	bookmarks = user.bookmark_set.all()


	template = get_template('user_page.html')
	variables = Context({ 
		'username' : username,
		'bookmarks': bookmarks 
	})
	
	output = template.render(variables)
	return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')