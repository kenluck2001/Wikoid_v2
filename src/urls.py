import os

from Wikoid import settings
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Wikoid.views.home', name='home'),
    # url(r'^Wikoid/', include('Wikoid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
		{ 'document_root' : os.path.join(settings.CURRENT_PATH, 'static') }
	),
	#url(r'^results/(.*)/$', 'Wikoid.views.results', name='jsonload'),

    (r'^index/$', 'Wikoid.views.indexView',{'template_name': 'index.html'}, 'index'),
    (r'^showpage/(.*)/$', 'Wikoid.views.showPage',{'template_name': 'results.html'}, 'Show Page'),

	#(r'^results/$', 'Wikoid.views.results', name='results'),
	#(r'^index/$', 'Wikoid.views.indexView',{'template_name': 'index.html'}, 'index'),

	#(r'^showpage/(.*)/$', 'Wikoid.views.showPage',{'template_name': 'showPage.html'}, 'Show Page'),

)
