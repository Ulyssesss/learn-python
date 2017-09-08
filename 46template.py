from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/sign_in', methods=['GET'])
def form():
    return render_template('form.html')


@app.route('/sign_in', methods=['POST'])
def sign_in():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('success.html', username=username, time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()
