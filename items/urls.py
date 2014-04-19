from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'/get/(?P<item_name>\w+)/$', 'items.views.get'),
	url(r'/search/$', "items.views.search"),

	)