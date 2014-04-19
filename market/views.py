from django.shortcuts import render_to_response
from items.models import Items
from django.http import HttpResponse
from django.core.context_processors import csrf


def home(request):
	c = {}
	c.update(csrf(request))
	c["name"] = "Easy-Shop Mall"
	return render_to_response('base.html', c)

def about(request):
	about = "We are members of Claflan!!!!! "
	return render_to_response('about.html', {"about": about})