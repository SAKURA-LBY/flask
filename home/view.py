from flask import url_for, g, current_app

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