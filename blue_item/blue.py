#!/usr/bin/env python

"""
FileName: blue
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 17:08:09
"""

from sanic import Blueprint
from .views import bar, bp_root, handle_request


bp = Blueprint('item', url_prefix='item')

bp.add_route(bar, "/endpoint")
bp.add_route(bp_root, "/app")
bp.add_route(handle_request, "/html")

