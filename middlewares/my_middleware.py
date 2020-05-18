#!/usr/bin/env python

"""
FileName: my_middleware
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 20:09:04
"""


async def print_on_request(request):
    """ 实现请求的前期处理，比如验证签名 """
    print("I print when a request is received by the server")


async def print_on_response(request, response):
    """ 实现响应的后续处理 """
    print("I print when a response is returned by the server")
