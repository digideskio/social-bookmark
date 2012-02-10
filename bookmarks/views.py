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
from bookmarks.forms import *

#generate the main page content
def main_page(request) :
    return render_to_response( 'main_page.html',RequestContext(request))

# Context is a object which can take Python Dictionary elements in the constructor)

# generate the user page content
def user_page(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		raise Http404(u'Requested user not found');
	bookmarks = user.bookmark_set.all()
	variables = RequestContext({ 'username' : username,	'bookmarks': bookmarks })
	return render_to_response('user_page.html', variables)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
	
def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email'])
			return HttpResponseRedirect('/register/success/')
		else:
			print "Form is not valid"
	else:
		form = RegistrationForm()
		variables = RequestContext(request, {'form':form})
		return render_to_response('registration/register.html',variables)
