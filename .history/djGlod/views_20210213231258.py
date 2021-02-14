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

    filename = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), 'templates', 'K_json.json')
    print(filename)

    def read_json(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.loads(f.readline(), encoding='utf-8')
    jsfile = read_json(filename)

    jf = [[1611590400000, 387.8, 389.2, 385.4, 386.7],
          [1611504000000, 385.75, 388.49, 383.8, 386.09],
          [1611244800000, 389.2, 389.64, 386.6, 387.69],
          [1611158400000, 384.9, 389.88, 382.14, 389.1],
          [1611072000000, 384.8, 386.4, 382.61, 386.06],
          [1610985600000, 384.08, 385.6, 383.32, 384.7],
          [1610899200000, 385.78, 386.05, 379.9, 384.15],
          [1610640000000, 383.68, 387.57, 383.3, 385.13],
          [1610553600000, 385.2, 387.77, 381.5, 383.68],
          [1610467200000, 387.21, 387.97, 383.56, 386.33]]

    return HttpResponse(json.dumps(jf))
