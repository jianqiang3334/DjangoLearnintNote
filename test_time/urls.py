from django.conf.urls import patterns, include, url
from test_show.views import hello
from test_show.views import current_datetime
from test_show.views import hours_ahead
from test_show.views import modul_1

"""from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_time.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
"""
urlpatterns=patterns('',(r'^hello/$',modul_1),(r'^time/$',current_datetime),(r'^time/plus/(\d{1,2})/$', hours_ahead),)