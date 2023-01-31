# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return '윤상현 개인서버 구축 대기중입니다.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

