# sanic-demo
sanic学习笔记及练习代码，基于blueprint实现模块间路由设置隔离。

main.py 混合了单个函数的使用

# 模块说明

## 应用模块
这里包含两个模块：
* blue_demo 
* blue_item

每个模块里包含：
* my_view.py -- 视图文件
* blue.py -- 当前模块内的路由配置
* lib.py -- 模块内的公用函数

## 中间件模块
middlewares -- 实现请求的前处理，或响应的后处理

## 公用库模块
lib -- 项目级公用方法，比如时间的相关处理。

## 配置模块
config.py -- 配置文件 

## 主模块

main.py -- 引用各个模块，启动服务。


# 运行方法

```shell script
pip install -r requirement.txt
python main.py
```

然后在浏览器中访问即可。可用的访问路径如下：

```html
http://0.0.0.0:8000/blue/endpoint
http://0.0.0.0:8000/blue/app
http://0.0.0.0:8000/blue/json
http://0.0.0.0:8000/blue/query_string?key1=value1&key2=value2
http://0.0.0.0:8000/blue/html

http://0.0.0.0:8000/item/html
http://0.0.0.0:8000/item/endpoint
http://0.0.0.0:8000/item/html

http://0.0.0.0:8000/demo/hello 
```
