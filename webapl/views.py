from flask import Flask
from webapl import app
from flask import render_template, request, flash, redirect, url_for
import re

@app.route("/")
def landing_page():
    return render_template('lp.html')

# 素数判定
@app.route("/", methods=["POST"])
def is_prime(n=0):
    result="素数です"
    data=request.form
    n=data.get("number")
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
                    flash("素数ではありません")
                else:
                    result="素数です"
                    
    return render_template("lp.html", result=result, num=n)   