from django.db import models
from django.contrib.auth.models import User
# requries a class derived from model.Model
# the URLField type must be unique
# This class is used to generate the schema in DB

class Link(models.Model):
	url = models.URLField(unique=True)

class Bookmark(models.Model):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User)
	link = models.ForeignKey(Link)
