from flask import Flask, render_template, request
import os.environ
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/result/', methods=['POST', 'GET'])
def result():
    error = None
    if request.method == 'POST':
        result = request.form
        for key, val in result.items():
            if key == 'name':
                name = val
            elif key == 'age':
                age = val
            elif key == 'favninja':
                ninja = val
        if name == '' or age == '' or ninja == '':
            error = 'Please fill in all fields.'
    return render_template("result.html", name=name, age=age,
                           ninja='Patrick Huston', error=error)


if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000)))
    app.run(host=HOST, port=PORT)
