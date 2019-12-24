from flask import Blueprint
# 1. 创建蓝图对象
home_blu=Blueprint("home_b",__name__,url_prefix='/home')


from . import view