#!/usr/bin/env python

"""
FileName: main
Author: deepinwst
Email: wanshitao@donews.com
Date: 2020/5/18 18:18:38
"""

from sanic import Sanic
from blue_demo.blue import bp as blue
from blue_item.blue import bp as item
import config

app = Sanic(__name__)

# 添加配置
app.config.from_object(config)

# 注册各个模块
app.blueprint(blue)
app.blueprint(item)

# 启动服务
app.run(host="0.0.0.0", port=8000, debug=True)
