from flask import Flask

app = Flask(__name__)

@app.route('/')
def raiz():
    return "Hello world! Carregando..."

@app.route('/add/<int:num1>/<int:num2>')
def add(num1:int, num2:int) -> str:
    return f"SOMA: {num1 + num2}"

@app.route('/sub/<int:num1>/<int:num2>')
def sub(num1:int, num2:int) -> str:
    return f"SUBTRAÇÃO: {num1 - num2}"

@app.route('/mul/<int:num1>/<int:num2>')
def mul(num1:int, num2:int) -> str:
    return f"PRODUTO: {num1 * num2}"

@app.route('/div/<int:num1>/<int:num2>')
def div(num1:int, num2:int) -> str:
    if num2==0:
        return f"O divisor não pode ser {num2} (zero)."
    return f"DIVISÃO: {num1 / num2}"
