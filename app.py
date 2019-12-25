

from flask import Flask, g, current_app

import tool
from config import config_dict

# 上下文变量: 有使用范围  [请求开始, 请求结束]
# 请求上下文: 记录一些和请求有关的数据 request session
# 应用上下文: 记录一些和应用有关的数据  current_app  g

# current_app:  会自动引用创建的Flask对象, 需要在项目的其他文件中使用app时, 应该通过current_app来获取  可以减少循环导入问题
# g: flask给开发者预留的一个容器, 用于记录自定义数据   g变量每次请求会重置数据
# g使用场景: 1> 在钩子函数和视图函数之间传递数据  2> 函数嵌套调用时传递数据
#工厂函数
from home import home_blu


def create_app(config_type):
    # 创建应用
    flask_app= Flask(__name__)
    # 根据类型取出对应的配资子类
    config_class = config_dict[config_type]
    # 加载配置
    flask_app.config.from_object(config_class)
    # 优点: 可以保护隐私配置   export ENV_CONFIG="隐私配置的文件路径"silent=True,配置加载也不报错
    flask_app.config.from_envvar('ENV_CONFIG',silent=True)

    flask_app.add_url_rule('/',hello_world.__name__,hello_world)

    # 应用注册蓝图对象
    flask_app.register_blueprint(home_blu)
    return flask_app

# app = create_app('dev')


# @app.route('/')
def hello_world():
    g.name = 'zs'
    tool.func1()
    print(current_app.config.get('SQL_URL'))
    print(current_app.config.get('SECRET_KEY'))
    return 'Hello World!'


if __name__ == '__main__':
    create_app('dev').run(debug=True)
