from flask import url_for, g, current_app
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from home import home_blu


@home_blu.route('/')
def index():
    print(g.name)
    print(current_app.url_map)
    return "index"

@home_blu.before_request
def home_prepare():
    g.name ="lby"
    print('home_prepare')


@home_blu.route('/demo1')
def demo1():
    # 细节2: 蓝图定义的路由, 其函数标记为 蓝图名.函数名
    url1 = url_for('home_b.demo1')
    print(url1)
    return 'demo1'
def deco1(f):
    def wrapper(*args,**kwargs):
        print('deco1')
        return f(*args,**kwargs)

    return wrapper
def deco2(f):
    def wrapper(*args,**kwargs):
        print('deco2')
        return f(*args,**kwargs)

    return wrapper
class DemoResource(Resource):

    method_decorators = {'get':[deco1,deco1],'post':[deco2]}


    def get(self):
        # 类视图响应的content-type默认变为json形式
        # 类视图的返回值可以是字典, 会被自动转为json字符串
        parser=RequestParser()

        parser.add_argument('name')
        parser.add_argument('age')

        args=parser.parse_args()

        return {'foo': 'get','name':args.name,'age':args.age}

    def post(self):
        parser = RequestParser()

        parser.add_argument('name',required=True,location='json')
        parser.add_argument('age',default=10)

        args = parser.parse_args()

        return {'foo': 'get', 'name': args.name, 'age': args.age}