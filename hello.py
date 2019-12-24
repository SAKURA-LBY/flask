from flask import Flask

app = Flask(__name__)


@app.route('/',methods=['post','get'])
def hello_world():
    return ('index')
@app.after_request
def after_request(response):
    # print(after_request)
    # return ('after_request')
    print("after_request")
    response.headers["Content-Type"] = "application/json"
    return response

@app.before_first_request
def before_first_request():
    print('before_first_request')

@app.before_request
def before_request():
    print('before_request')

@app.teardown_request
def teardown_request(error):
    return ('teardown_request : %s' % error)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
