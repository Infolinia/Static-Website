"""naukaJazdy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from reservation.views import reserve
from reservation.views import my
from home.views import home
from about.views import about
from gallery.views import gallery
from contact.views import contact
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^reserve/$', reserve),
    url(r'^my/$', my),
	url(r'^about/$', about),
	url(r'^gallery/$', gallery),
	url(r'^contact/$', contact),
   
	url( r'^accounts/login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
	url( r'^accounts/logout/$',views.logout),
	url( r'^accounts/loggedin/$',auth_views.LoginView.as_view(template_name="loggedin.html")),
	url(r'^accounts/auth/$', views.view_auth),
	
	url(r'^accounts/create_user/$', views.create_user),
	

	url(r'^$', home), 
]
