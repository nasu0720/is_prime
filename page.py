from flask import Flask
from flask import render_template, request
import re
app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('lp.html')
# 素数判定
@app.route("/result", methods=["POST"])
def is_prime(n=0):
    data=request.form
    n=data.get("number")
    result="素数です"
    match=re.fullmatch(r'^[1-9][0-9]*$',str(n))
    if match==None:
        result="自然数を入力してください"
    
    else:
        n=int(n)    
        if n < 2:
            result="素数ではありません"

        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    result="素数ではありません"

    return render_template('result.html', result=result)