from flask import Flask, render_template, request 
import re 
 
app = Flask(__name__)
 
@app.route('/') 
def home():
    return render_template('calculator.html',  result='')
 
@app.route('/calculate',  methods=['POST'])
def calculate():
    expression = request.form.get('expression',  '')
    print(expression)
    if not expression:
        return ''
    
    # 安全性检查：只允许数字、运算符和小数点 
    allowed_chars = set('0123456789+-*/().')
    if not all(c in allowed_chars for c in expression):
        return '错误'
    
    try:
        result = eval(expression)
        return str(result)
    except:
        return '错误'
 
if __name__ == '__main__':
    app.run(debug=True) 