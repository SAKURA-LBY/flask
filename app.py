from flask import Flask, g

import tool
from home import home_blu
# 上下文变量: 有使用范围  [请求开始, 请求结束]
# 请求上下文: 记录一些和请求有关的数据 request session
# 应用上下文: 记录一些和应用有关的数据  current_app  g

# current_app:  会自动引用创建的Flask对象, 需要在项目的其他文件中使用app时, 应该通过current_app来获取  可以减少循环导入问题
# g: flask给开发者预留的一个容器, 用于记录自定义数据   g变量每次请求会重置数据
# g使用场景: 1> 在钩子函数和视图函数之间传递数据  2> 函数嵌套调用时传递数据
app = Flask(__name__)


@app.route('/')
def hello_world():
    g.name = 'zs'
    tool.func1()
    return 'Hello World!'
# 应用注册蓝图对象
app.register_blueprint(home_blu)

if __name__ == '__main__':
    app.run(debug=True)
