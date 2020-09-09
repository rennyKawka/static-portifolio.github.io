from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1 style="color: Blue">hey u!!!</h1>'

if __name__ == "__main__":
    app.run()