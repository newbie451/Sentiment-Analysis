from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','app.views.home'),
    url(r'^keyword','app.views.keyword'),
    url(r'^textword','app.views.text'),
    url(r'^keyres','app.views.keyres'),
    url(r'^textres','app.views.textres'),
    url(r'^normalres','app.views.normalres'),
]