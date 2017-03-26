"""pin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from board.views import saveval
from board.views import login,auth_view,loggedin,invalid_login,forgot_pass,welcome
from board.views import upload_file,success_upload,retrieve,delete,pinions,edit,upload,logout
from board.views import update_file,edit_profile,update_profile,display_cat,retrieve_art
from board.views import retrieve_food,retrieve_other,pin_it,help_pin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from board import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^pinions/',pinions),
	url(r'^help_pin/',help_pin),
	url(r'^retrieve_art/$', retrieve_art),
    url(r'^retrieve_food/$', retrieve_food),
    url(r'^retrieve_other/$', retrieve_other),
	url(r'^display_cat/$',display_cat),
    url(r'^saveval/$',saveval),         #(?P<username>[a-zA-Z0-9&. ]+)
    #url(r'^thanks/$',thanks),
	url(r'^login/$', login),
	url(r'^welcome/$', welcome),
	url(r'^forgot_pass/$', forgot_pass),
	url(r'^auth/$', auth_view),
	url(r'^logout/$', logout),
	url(r'^loggedin/$', loggedin),
	url(r'^invalid_login/$', invalid_login),
	url(r'^upload/$',upload),
	url(r'^upload_file/$',upload_file),
	url(r'^edit/(?P<edit_link>[a-zA-z&.0-9 ]+)/$',edit),
    url(r'^success_upload/$',success_upload),
    url(r'^profile/$',retrieve),
	url(r'^delete/(?P<del_link>[a-zA-Z&.]+)/$',delete),
	#url(r'^edit/(?P<edit_link>[a-zA-z&.0-9]+)/$',edit),
	url(r'^update_file/(?P<edit_link>[a-zA-z&.0-9]+)/$',update_file),
	url(r'^edit_profile/$',edit_profile),
	url(r'^update_profile/$',update_profile),
	url(r'^pin_it/(?P<pin_link>[a-zA-z&.0-9]+)/$',pin_it),
	
)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
	
	
