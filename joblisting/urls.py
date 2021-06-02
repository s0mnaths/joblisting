"""joblisting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from jobs.views import HomePageView, JobDetails
from jobs.admin_views import DashBoardView, SettingsView, AdminView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='index'),
    url(r'^details/([\w\-]+)/?$', JobDetails.as_view(), name='index'),

    url(r'^admin/settings', SettingsView.as_view(), name='settings'),
    url(r'^admin/create', AdminView.as_view(), name='create'),
    url(r'^admin/', DashBoardView.as_view(), name='admin'),

]
