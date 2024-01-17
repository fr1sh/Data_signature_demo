from flask import Flask,request, jsonify
from  flask import  render_template
from flask_cors import CORS
import hmac
import hashlib
import base64

app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def index():
    return  render_template('index.html')

@app.route('/level-0')
def demo0():
    return  render_template('demo0.html')

@app.route('/level-1')
def demo1():
    return  render_template('demo1.html')

@app.route('/level-2')
def demo2():
    return  render_template('demo2.html')

@app.route('/level-3')
def demo3():
    return  render_template('demo3.html')

@app.route('/login0',methods=['POST','GET'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "123456":
        return jsonify({"status": "success", "message": "登录成功"})
    else:
        return jsonify({"status": "failure", "message": "登录失败，请检查账号和密码"})

@app.route('/login1',methods=['POST'])
def login1():
    data = request.get_json()
    secret_key = b'1234567890abcdefghijk'  # 替换为实际的密钥
    username = data.get("username")
    password = data.get("password")
    signature = data.get("signature")

    # 构建用于签名的数据
    data_to_sign = username + password
    # 使用 HMAC SHA-256 进行解密验证签名
    expected_signature = hmac.new(secret_key, data_to_sign.encode(), hashlib.sha256).digest()

    # 将计算得到的签名与前端传递的签名进行比较
    if base64.b64encode(expected_signature) == signature.encode():
        if username == "admin" and password == "123456":
            return jsonify({"status": "success", "message": "登录成功"})
        else:
            return jsonify({"status": "failure", "message": "登录失败，请检查账号和密码"})
    else:
        return jsonify({"status": "failure", "message": "签名失败，请勿篡改数据"})
    return  render_template('demo1.html')


if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', port='8000',debug=False)