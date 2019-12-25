from flask import Blueprint
# 1. 创建蓝图对象
from flask_restful import Api



home_blu=Blueprint("home_b",__name__,url_prefix='/home')


# 1. 创建API对象  用于管理类视图(资源)
blu = Api(home_blu)
from home.view import DemoResource
blu.add_resource(DemoResource, '/t1', endpoint='demo')


from . import view
