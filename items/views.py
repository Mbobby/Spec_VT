from django.shortcuts import render_to_response
from items.models import Items
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
# Create your views here.

def get(request, item_name):
	try:
		n = Items.objects.get(name = item_name.lower())
		return render_to_response('get.html', { "item" : n})
	except:
		c = {}
		c.update(csrf(request))
		c['message'] = "The product you are searching for is not being offered by us!"
		return render_to_response('base.html', c)
	

def search(request):
	if request.method == "POST":
		item = request.POST['item'].strip()
		if (len(item) > 0):
			return HttpResponseRedirect('/items/get/%s/' % item)
		else:
			return HttpResponseRedirect('/home/')
	else:
		return HttpResponseRedirect('/home/')