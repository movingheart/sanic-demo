#!/usr/bin/env python

"""
FileName: funcs
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 18:24:55
"""

from sanic.response import json, text
from sanic.log import logger
from sanic import response

from lib.pub_time import now_time_str
from .lib import print_myself


async def bar(request):
    return text(request.endpoint)


async def bp_root(request):
    if request.app.config['DEBUG']:
        logger.info("time:{}".format(now_time_str()))
        return json({'status': 'debug', 'time': now_time_str()})
    else:
        return json({'status': 'production', 'time': now_time_str()})


def post_json(request):
    return json({'received': True, "message": request.json})


def query_string(request):
    return json({"parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string})


def handle_request(request):
    return response.html('<p>Hello world!</p><p>{}</p>'.format(print_myself()))
