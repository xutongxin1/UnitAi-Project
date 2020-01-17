"""
    没有设置session时，获取session就是None
"""

from flask import Flask, session

app = Flask(__name__)

"""
    在flask当中使用 session 时，必须要做一个配置、
    即 flask的session中需要用到的秘钥字符串，可以是任意值
    flask默认把数据存放到了cookie中
"""

app.config["SECRET_KEY"] = "renyizifuchuan"


@app.route("/login")
def login():
    """设置session的数据"""
    session["name"] = "python"
    session["mobile"] = "18612345678"
    return "login success"


@app.route("/index")
def index():
    """获取session的数据"""
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True,port=19150)