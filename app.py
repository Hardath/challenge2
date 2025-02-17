from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo à página inicial!'

@app.route('/login')
def login():
    return 'Página de login!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

