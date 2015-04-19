from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
	def get_success_url(self, request, user):
		return '/rango/add_profile/'


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)


if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
	)