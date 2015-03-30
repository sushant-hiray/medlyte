from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medlyte.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', 'provider_auth.views.account_profile', name='account_profile'),
    
    url(r'^member/$', 'medlyte.views.member_index', name='user_home'),
    url(r'^member/action$', 'medlyte.views.member_action', name='user_action'),

    url(r'^$', include('website.urls')),
)
