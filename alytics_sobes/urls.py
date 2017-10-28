"""alytics_sobes URL Configuration

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

from jamshid.views import RunChecks
from ravshan.views import DataSetsList, DataSetUpload, DataSetDelete

urlpatterns = [
    url(r'^$', DataSetsList.as_view(), name='datasets_list'),
    url(r'^upload/$', DataSetUpload.as_view(), name='dataset_upload'),
    url(r'^delete/(?P<pk>[0-9]*)$', DataSetDelete.as_view(), name='dataset_delete'),
    url(r'^run_checks/$', RunChecks.as_view(), name='run_checks'),

    url(r'^admin/', admin.site.urls),
]
