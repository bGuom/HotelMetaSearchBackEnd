# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

import scripts.Main as MainScript

def index(request):
    search = request.GET.get('search_query', '')
    checkinyear = request.GET.get('checkin_year', '2019')
    checkinmonth = request.GET.get('checkin_month', '')
    checkinday = request.GET.get('checkin_day', '')
    checkoutyear = request.GET.get('checkout_year', '2019')
    checkoutmonth = request.GET.get('checkout_month', '')
    checkoutday = request.GET.get('checkout_day', '')
    rooms = request.GET.get('rooms', '')
    adults = request.GET.get('adults', '')
    children = request.GET.get('children', '0')

    return HttpResponse(MainScript.search(search,checkinyear,checkinmonth,checkinday,checkoutyear,checkoutmonth,checkoutday,rooms,adults,children))
    
    
# Create your views here.
