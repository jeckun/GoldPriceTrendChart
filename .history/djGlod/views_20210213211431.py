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
        [1317600000, 380.37, 382.64, 373.17, 374.60],
        [1317686400, 374.57, 381.80, 354.24, 372.50],
        [1317772800, 367.86, 379.82, 360.30, 378.25],
        [1317859200, 373.33, 384.78, 371.80, 377.37],
        [1317945600, 375.78, 377.74, 368.49, 369.80],
        [1318204800, 379.09, 388.81, 378.21, 388.81],
        [1318291200, 392.57, 403.18, 391.50, 400.29],
        [1318377600, 407.34, 409.25, 400.14, 402.19],
        [1318464000, 404.98, 408.43, 402.85, 408.43],
        [1318550400, 416.83, 422.00, 415.27, 422.00],
        [1318809600, 421.74, 426.70, 415.94, 419.99],
        [1318896000, 421.76, 424.81, 415.99, 422.24],
    ]
    # filename = os.path.join(os.path.dirname(os.path.dirname(
    #     os.path.abspath(__file__))), 'templates', 'jsonp.json')
    # print(filename)

    # def read_json(filename):
    #     with open(filename, 'r', encoding='utf-8') as f:
    #         return json.loads(f.readline(), encoding='utf-8')
    # js = read_json(filename)
    return HttpResponse(json.dumps(jsfile))
