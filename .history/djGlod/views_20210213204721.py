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
    filename = ''
    print(os.path.abspath(__file__))

    def read_json(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.loads(f.readline(), encoding='utf-8')
    return HttpResponse(read_json(filename))
