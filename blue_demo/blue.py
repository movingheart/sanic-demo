#!/usr/bin/env python

"""
FileName: blue
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 17:08:09
"""

from sanic import Blueprint
from .views import bar, bp_root, post_json, query_string, handle_request


bp = Blueprint('my_blue', url_prefix='blue')

bp.add_route(bar, "/endpoint")
bp.add_route(bp_root, "/app")
bp.add_route(post_json, "/json")
bp.add_route(query_string, "/query_string")
bp.add_route(handle_request, "/html")

