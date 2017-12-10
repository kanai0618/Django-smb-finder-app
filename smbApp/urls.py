from django.conf.urls import url
from smbApp import views

urlpatterns = [
    url(r'^smbfinder/mca/(?P<company_name>.+?)/$', views.mca_smb_details),
    url(r'^smbfinder/fb/(?P<company_name>.+?)/$', views.fb_smb_details),
    url(r'^$', views.HomePageView.as_view()),
]
