# -*- coding: utf-8 -*-
import os
import json
from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello world ! ")


def runoob(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


def get_json(request):
    jsfile = [
        [1317600000000, 380.37, 382.64, 373.17, 374.60],
        [1317686400000, 374.57, 381.80, 354.24, 372.50],
        [1317772800000, 367.86, 379.82, 360.30, 378.25],
        [1317859200000, 373.33, 384.78, 371.80, 377.37],
        [1317945600000, 375.78, 377.74, 368.49, 369.80],
    ]
    return HttpResponse(json.dumps(jsfile))
