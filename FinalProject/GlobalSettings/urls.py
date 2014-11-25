from django.conf.urls import patterns, include, url
from DisplayAndInteractive import views
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

	url(r'^$', 'DisplayAndInteractive.views.home', name = 'index'),
    # url(r'^$', 'GlobalSettings.views.home', name='home'),
    # url(r'^GlobalSettings/', include('GlobalSettings.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
