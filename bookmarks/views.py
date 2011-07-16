# Create your views here.
from django.http import HttpResponse
def main_page(request) :
	output = u'''
		<html>
			<head><Title>%s</Title></head>
			<body>  
				<h1>%s</h1><p>%s</p>
			</body>
		</html>
	''' % ( 
	u'Django-Bookmarks',
	u'Weclome to django bookmarks',
	u'Where you can store and share bookmarks!'
	)
	return HttpResponse(output)
