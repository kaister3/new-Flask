from flask import Flask
from flask import escape, url_for
app = Flask(__name__)

@app.route('/user/<name>')
def user_page(name):
    return '%s' %name

@app.route('/')
def hello():
    # 返回值作为响应的主体，默认会被浏览器作为 HTML 格式解析
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='kay'))
    print(url_for('test_url_for'))

if __name__ == "__main__":
    app.run()