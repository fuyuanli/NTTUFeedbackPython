#!/usr/bin/python3
from infosysfunc import *

import os
import sys
from flask import Flask, request, send_from_directory
from flask import render_template
from flask import send_file
import logging
import getpass

infosysurl = "https://infosys.nttu.edu.tw/"
captcha = infosysurl+"Captcha.ashx?code="+str(random.random())
 
app = Flask(__name__,static_url_path='/static')

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    
    return render_template('stop.html')
    #return render_template('index.html')

@app.route('/get_code')
def get_code():
    global s
    s = requests.Session()
    getCode(captcha,s)
        
    path = str(os.getenv("OPENSHIFT_DATA_DIR"))+'code.png'
    return send_file(path, mimetype='image/png') 

@app.route('/nttu', methods=['POST'])
def nttu():
    uid = str(request.form['uid'])
    if len(uid)!=8:
        uid="00000000"
    
    passwd = str(request.form['passwd'])
    
    code = str(request.form['code'])
    if len(code)!=4:
        code="0000"
    
    accept = int(request.form['accept'])
    if(accept==1):
        try:
            message = infosys(s,uid,passwd,code)
            message = "<h2>填表完成，請上<a href='https://infosys.nttu.edu.tw/' target='_blank'>校務系統</a>檢查</h2>" + message
            return render_template('2.html',message=message) 

        except:
            message = "填表失敗，打錯帳號密碼，還是驗證碼？"
            return render_template('2.html',message=message) 
    else:
        message = "同意條款才能使用喔！"
        return render_template('2.html',message=message) 
 
if __name__ == '__main__':
    app.run(threaded=True)

