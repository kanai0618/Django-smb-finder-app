# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView
from django.http import HttpResponse

from functions import *
from functions.fb_smb_details import *
from functions.mca_details import *
from functions.industry_code_mapping import *
# Create your views here.


def HelloWorld(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mca_smb_details(request,company_name):
    mca_details = McaDetails()
    mca_details_response = mca_details.mca_details_fetch(company_name)
    return HttpResponse(mca_details_response)


def fb_smb_details(request,company_name):
    fb_details = FbSmbDetails()
    fb_details_response = fb_details.fb_smb_details_fetch(company_name)
    return HttpResponse(fb_details_response)


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
