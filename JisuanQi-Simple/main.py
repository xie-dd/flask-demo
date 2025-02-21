from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def calculator():
    num1 = ""
    num2 = ""
    operation = "+"
    result = ""

    if request.method  == 'POST':
        if 'num1' in request.form  and 'num2' in request.form  and 'operation' in request.form: 
            num1 = request.form['num1'] 
            num2 = request.form['num2'] 
            operation = request.form['operation'] 

            try:
                num1_float = float(num1)
                num2_float = float(num2)

                if operation == '+':
                    result = num1_float + num2_float 
                elif operation == '-':
                    result = num1_float - num2_float 
                elif operation == '*':
                    result = num1_float * num2_float 
                elif operation == '/':
                    if num2_float != 0:
                        result = num1_float / num2_float 
                    else:
                        result = "除数不能为零！"
                else:
                    result = "无效的操作符！"
            except ValueError:
                result = "请输入有效的数字！"

    return render_template('calculator.html',  
                         num1=num1, 
                         num2=num2, 
                         operation=operation,
                         result=result)

if __name__ == '__main__':
    app.run(debug=True) 