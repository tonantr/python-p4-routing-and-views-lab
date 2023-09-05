#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    if parameter == 10:
        # return '\n'.join(str(i) for i in range(10))
        return '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n'
    else:
        return str(parameter)

@app.route('/math/<path:parameter>')
def math(parameter):
    params = parameter.split('/')
    if len(params) == 3 and params[1] == '+':
        num1 = int(params[0])
        num2 = int(params[2])
        result = num1 + num2
        return f'{result}'
    elif len(params) == 3 and params[1] == '-':
        num1 = int(params[0])
        num2 = int(params[2])
        result = num1 - num2
        return f'{result}'
    elif len(params) == 3 and params[1] == '*':
        num1 = int(params[0])
        num2 = int(params[2])
        result = num1 * num2
        return f'{result}'
    elif len(params) == 3 and params[1] == 'div':
        num1 = int(params[0])
        num2 = int(params[2])
        result = num1 / num2
        return f'{result}'
    elif len(params) == 3 and params[1] == '%':
        num1 = int(params[0])
        num2 = int(params[2])
        result = num1 % num2
        return f'{result}'
    return parameter



if __name__ == '__main__':
    app.run(port=5555, debug=True)
