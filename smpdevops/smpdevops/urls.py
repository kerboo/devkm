from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import *
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',Login,name='Login'),
    url(r'logout/$', Logout, name='Logout'),
#    url(r'^asset/',include('smp_assets.urls')),
    url(r'^accounts/',include('accounts.urls')),
)
