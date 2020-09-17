#!/usr/bin/env python

"""
FileName: main
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 18:18:38
"""

from sanic import Sanic
from sanic.response import html

from blue_demo.blue import bp as blue
from blue_item.blue import bp as item
import config
from middlewares.my_middleware import print_on_request, print_on_response

app = Sanic(__name__)

# 添加配置
app.config.from_object(config)

# 注册中间件
app.register_middleware(print_on_request, attach_to='request')
app.register_middleware(print_on_response, attach_to='response')

# 注册各个模块
app.blueprint(blue)
app.blueprint(item)


# 混合添加单个函数
async def hello(request):
    return html("<h1>Hello</h1>")
app.add_route(hello, "/demo/hello", methods=['GET'])

# 启动服务
app.run(host="0.0.0.0", port=8000, debug=True)
