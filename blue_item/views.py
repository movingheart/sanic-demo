#!/usr/bin/env python

"""
FileName: my_view
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 19:21:41
"""

from sanic import response

from sanic.response import json, text
from lib.pub_time import now_timestamp
from .lib import print_myself


async def bar(request):
    return text(request.endpoint)


async def bp_root(request):
    if request.app.config['DEBUG']:
        return json({'status': 'debug', 'module': 'module1', 'timestamp': now_timestamp()})
    else:
        return json({'status': 'production', 'module': 'module1', 'timestamp': now_timestamp()})


def handle_request(request):
    return response.html('<p>Hello world!</p><p>{}</p>'.format(print_myself()))
