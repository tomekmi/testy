from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apptesty.views.home', name='home'),
    url(r'^test/(?P<tid>[0-9]+)$', 'apptesty.views.solvetest', name='solvetest'),
    url(r'^test/(?P<tid>[0-9]+)/check$', 'apptesty.views.solvetestcheck', name='solvetestcheck'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
