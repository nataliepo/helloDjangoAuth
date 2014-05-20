from django.conf.urls import patterns, include, url

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),                                          # we absolutely need these ones

    url(r'^$', TemplateView.as_view(template_name="login.html")),                   # also fairly important
    url(r'^logout/$', logout, {'next_page': '/'}, name='gauth_logout'),             # this one is nice, but not totally required

    url(r'^login-error/$', TemplateView.as_view(template_name="login-error.html")), # if you've set up messages, you could loop through them here

    # Now we can test whether this stuff works
    url(r'^secrets$', login_required(TemplateView.as_view(template_name="secrets.html"))),  


   
    
    
)
