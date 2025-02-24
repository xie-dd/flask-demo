# flask-demo





# 项目1：JiSuanQi



## 1. 项目概述

本项目旨在创建一个简单的计算器 Web 应用，用户可以通过浏览器界面输入数学表达式并得到计算结果。前端使用 HTML 和 JavaScript 构建用户界面，后端使用 Flask 框架处理计算逻辑。

![image-20250221120516508](https://mypic2016.oss-cn-beijing.aliyuncs.com/picGo/202502211205428.png)



## 2. 环境准备

在开始之前，请确保以下工具已安装：

- **Python 3.x**：可以从 [Python 官方网站](https://www.python.org/) 下载
- **Flask**：使用 pip 安装：`pip install flask`
- **文本编辑器或 IDE**：如 VS Code、PyCharm 等

------

## 3. HTML 文件解析

### 3.1 HTML 结构分析

```
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>计算器</title>
    <style>
        /* CSS 样式代码 */
    </style>
</head>
<body>
    <div class="calculator">
        <form id="calculatorForm">
            <input type="text" id="display" name="expression" readonly value="{{ result }}">
            <div class="buttons">
                <button type="button" class="clear" onclick="clearDisplay()">C</button>
                <button type="button" onclick="deleteLastChar()">←</button>
                <button type="button" onclick="appendToDisplay('(')">(</button>
                <button type="button" onclick="appendToDisplay(')')">)</button>
                
                <!-- 第一行 -->
                <button type="button" onclick="appendToDisplay('7')">7</button>
                <button type="button" onclick="appendToDisplay('8')">8</button>
                <button type="button" onclick="appendToDisplay('9')">9</button>
                <button type="button" class="operator" onclick="appendToDisplay('/')">/</button>
 
                <!-- 第二行 -->
                <button type="button" onclick="appendToDisplay('4')">4</button>
                <button type="button" onclick="appendToDisplay('5')">5</button>
                <button type="button" onclick="appendToDisplay('6')">6</button>
                <button type="button" class="operator" onclick="appendToDisplay('*')">×</button>
                
                <!-- 第三行 -->
                <button type="button" onclick="appendToDisplay('1')">1</button>
                <button type="button" onclick="appendToDisplay('2')">2</button>
                <button type="button" onclick="appendToDisplay('3')">3</button>
                <button type="button" class="operator" onclick="appendToDisplay('-')">-</button>
                
                <!-- 第四行 -->
                <button type="button" onclick="appendToDisplay('0')">0</button>
                <button type="button" onclick="appendToDisplay('00')">00</button>
                <button type="button" class="equals" onclick="calculate()">=</button>
                <button type="button" class="operator" onclick="appendToDisplay('+')">+</button>
                
            </div>
        </form>
    </div>
    <script>
        function appendToDisplay(value) {
            document.getElementById('display').value  += value;
        }
 
        function clearDisplay() {
            document.getElementById('display').value  = '';
        }
 
        function deleteLastChar() {
            const display = document.getElementById('display'); 
            display.value  = display.value.slice(0,  -1);
        }
 
        async function calculate() {
            const expression = document.getElementById('display').value; 
            try {
                const response = await fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: `expression=${encodeURIComponent(expression)}`
                });
                const result = await response.text(); 
                document.getElementById('display').value  = result;
            } catch (error) {
                console.error(' 计算错误:', error);
                document.getElementById('display').value  = '错误';
            }
        }
    </script>
</body>
</html>
```

#### 主要元素

- **输入框 (`#display`)**：用于显示当前输入的表达式和计算结果。
- **按钮 (`button`)**：包括数字按钮、运算符按钮、清空按钮 (`C`)、删除按钮 (`←`) 和等于号按钮 (`=`)。
- **表单 (`form`)**：用于将输入的表达式提交到后端。

### 3.2 HTML 中的关键功能

#### 输入框 (`#display`)

```
<input type="text" id="display" name="expression" readonly value="{{ result }}">
```

- `type="text"`：定义这是一个文本输入框。
- `id="display"`：用于 JavaScript 中定位该元素。
- `name="expression"`：表单提交时使用的字段名。
- `readonly`：防止用户手动输入，只能通过按钮操作。
- `value="{{ result }}"`：从 Flask 后端传递的计算结果。

#### 按钮 (`button`)

```
<button type="button" class="clear" onclick="clearDisplay()">C</button>
<button type="button" onclick="deleteLastChar()">←</button>
<button type="button" onclick="appendToDisplay('(')">(</button>
<button type="button" onclick="appendToDisplay(')')">)</button>
...
```

- `type="button"`：定义这是一个普通按钮。
- `class`：用于 CSS 样式区分不同类型的按钮。
- `onclick`：绑定点击事件，执行相应的 JavaScript 函数。

#### 表单 (`form`)

```
<form id="calculatorForm">
```

- `id="calculatorForm"`：用于 JavaScript 中定位该表单。
- 表单中的数据通过 POST 方法提交到后端 `/calculate` 路由。

### 3.3 JavaScript 功能

```
function appendToDisplay(value) {
    document.getElementById('display').value  += value;
}
 
function clearDisplay() {
    document.getElementById('display').value  = '';
}
 
function deleteLastChar() {
    const display = document.getElementById('display');  
    display.value  = display.value.slice(0,  -1);
}
 
async function calculate() {
    const expression = document.getElementById('display').value;  
    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `expression=${encodeURIComponent(expression)}`
        });
        const result = await response.text();  
        document.getElementById('display').value  = result;
    } catch (error) {
        console.error('  计算错误:', error);
        document.getElementById('display').value  = '错误';
    }
}
```

#### 主要函数

1. appendToDisplay(value)

   - 向输入框追加字符。
   - 示例：点击 `7` 按钮时，调用 `appendToDisplay('7')`。
   
2. clearDisplay()

   - 清空输入框。
   - 示例：点击 `C` 按钮时，调用 `clearDisplay()`。
   
3. deleteLastChar()

   - 删除输入框最后一个字符。
   - 示例：点击 `←` 按钮时，调用 `deleteLastChar()`。
   
4. calculate()

   - 发送 POST 请求到后端进行计算。
   - 使用 `fetch` API 发送请求，并等待响应。
   - 更新输入框显示计算结果或错误信息。

------

## 4. Flask 后端解析

### 4.1 项目结构

```
my_calculator/
├── app.py  
└── templates/
    └── calculator.html  
```

### 4.2 Flask 应用代码

```
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
```

------

## 5. 功能实现步骤

### 5.1 启动 Flask 应用

在终端中导航到项目目录并运行：

```
python app.py  
```

应用将在 `http://localhost:5000` 上启动。

### 5.2 使用 async 的目的

在前端 JavaScript 中，`async` 函数用于处理异步操作（如网络请求）。以下是使用 `async` 的主要目的：

1. 计算器使用JavaScript的`fetch`方法发送异步请求到Flask后端进行计算。这意味着每当用户点击等于号按钮时，会触发`calculate()`函数，这个函数使用`fetch`发送一个POST请求，等待响应，然后更新显示结果。这种方法的好处是页面不需要刷新，用户体验流畅。 但是用户希望移除`async`，改用表单提交的方式。这意味着每次点击等于号时，整个表单会被提交到后端，服务器处理完后返回结果，然后页面可能会刷新或者部分内容更新。这可能会影响用户体验，因为页面刷新会导致用户需要重新输入数据。

2. 简化异步代码处理网络请求

   - 使用 `async/await` 可以让异步代码看起来更像同步代码，提高可读性。

   - 使用 `fetch` 发送网络请求是一个异步操作。

   - `async/await` 可以让代码等待请求完成后再继续执行后续操作。

   - 示例：
 ```js
 async function calculate() {
     const response = await fetch('/calculate');
     const result = await response.text(); 
     // 处理结果 
 }
 ```




## 6. 知识点

1. CSS类选择器与标签选择器

   - `.buttons`：这是一个 CSS 类选择器，表示对所有带有 `class="buttons"` 的 HTML 元素应用以下样式。

```css
.buttons {
    display: grid;           /*网格布局*/
    grid-template-columns: repeat(4, 1fr);  /*总共有 4 列，每列宽度相同*/
    gap: 5px;               /*设置网格项之间的间距（间隙）为 5 像素*/
}
```

   - `button` 这是一个标签选择器，表示对所有 `<button>` 元素应用以下样式。

```
button {
    padding: 15px;
    font-size: 18px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    background-color: #f8f8f8;
    color: #333;
}
```



2. CSS鼠标悬停 hover

```
.operator与.operator:hover
button与button:hover
```

- 触发条件与用途

  - `.operator`：无需任何交互，默认应用。设置元素的默认样式。
  - `.operator:hover`：仅在鼠标悬停时应用。设计交互效果，增强用户体验。

  

3. 可以使用`async`来显示计算结果，避免刷新页面
4. 使用form进行表单提交时，不一定非要有一个submit标签，这个计算器就没有.
5. 使用form进行表单提交时，要像下面这样，有name与value

```
<input type="text" id="display" name="expression" readonly value="{{ result }}">
```



# 项目 2：简易计算器

![image-20250221194251742](https://mypic2016.oss-cn-beijing.aliyuncs.com/picGo/202502211942988.png)



## 主要代码

### HTML文件

```
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>Flask Calculator</title>
    <style>
      ...
    </style>
</head>
<body>
    <div class="calculator">
        <h2>简单计算器</h2>
        <form method="post">
            <input type="number" name="num1" placeholder="请输入第一个数字" value="{{ num1 }}" required><br>
            <input type="number" name="num2" placeholder="请输入第二个数字" value="{{ num2 }}" required><br>
            <select name="operation">
                <option value="+"{% if operation == '+' %} selected{% endif %}>加法 (+)</option>
                <option value="-"{% if operation == '-' %} selected{% endif %}>减法 (-)</option>
                <option value="*"{% if operation == '*' %} selected{% endif %}>乘法 (*)</option>
                <option value="/"{% if operation == '/' %} selected{% endif %}>除法 (/)</option>
            </select><br>
            <button type="submit" name="submit" value="calculate">等于 (=)</button>
        </form>
        <div id="result">
            {{ result }}
        </div>
    </div>
</body>
</html>
```



### main.py文件

```
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
```









## 知识点

1. 不使用异步提交async的方式，直接在后端保存表单数据并在重新渲染页面时回填。
2. 数据如何在前后端传递
3. 启动flask方式有两种
   - `flask run`这种情况适合虚拟环境中只有一个app.py文件的项目，像我现在学习flask，可能一个虚拟环境有多个项目，就不能使用这种方式，否则，每次都是启动的第一个app.py项目。这也要求所有项目的入口文件都不能是 app.py
   - `python main`这是所有python项目都可以使用的，我们现在多案例情况就使用这种方式来启动我们指定的某一个案例



# 项目3 ToDo

![](https://mypic2016.oss-cn-beijing.aliyuncs.com/picGo/202502242219035.png)



只需要在1panel中或者本地写个脚本获取mysql数据并进行检测发邮件即可



