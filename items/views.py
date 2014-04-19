from django.shortcuts import render
from items.models import Items
from django.http import HttpResponse
# Create your views here.

def get(request, name_item):
	try:
		n = Items.objects.get(name = name_item.lower())
		return HttpResponse(n.location)
	except:
		return HttpResponse("The item %s can not be found in this shop." % name_item)
