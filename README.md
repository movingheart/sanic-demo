# sanic-demo
sanic学习笔记及练习代码，基于blueprint实现路由的设置。

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
