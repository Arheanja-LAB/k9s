from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message='¡Hola, Minikube!')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
